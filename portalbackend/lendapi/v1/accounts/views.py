import datetime
import json
import re
import pyotp
import random

from functools import reduce

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q
from django.http import Http404
from django.utils import timezone
from django.utils.timezone import utc
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import views
from rest_framework.permissions import AllowAny, IsAuthenticated
import uuid

from portalbackend.lendapi.accounts.models import Company, User, CompanyMeta, Contact, EspressoContact, \
    ForgotPasswordRequest, UserSession, ScheduledMaintenance
from portalbackend.lendapi.constants import FORGOT_PASSWORD_EMAIL_BODY, APP_NAME,SESSION_EXPIRE_MINUTES
from portalbackend.lendapi.utils import PageNumberPaginationDataOnly
from portalbackend.lendapi.v1.accounting.utils import Utils
from portalbackend.settings import FORGOT_PASSWORD_EMAIL_URL
from .filters import CompanyFilter
from .permissions import IsAuthenticatedOrCreate
from .serializers import CompanySerializer, UserSerializer, CompanyMetaSerializer, \
    UserLoginSerializer, LoginSerializer, CreateUserSerializer, ContactSerializer, EspressoContactSerializer, \
    ForgotPasswordSerializer, ForgotPasswordValidationSerializer
from portalbackend.lendapi import constants
from portalbackend import settings
from django.contrib.auth import logout


class UserList(generics.ListCreateAPIView):
    """
    Lists all users
    """
    # permission_classes = (IsAuthenticatedOrCreate, )
    pagination_class = PageNumberPaginationDataOnly
    # queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('company', 'username', 'first_name', 'last_name', 'company__name')

    '''def post(self, request, *args, **kwargs):
        """
        Creates a new User
        """
        self.serializer_class = CreateUserSerializer
        return super(UserList, self).post(request)'''

    def get(self, request, *args, **kwargs):
        try:
            queryset = User.objects.all().order_by('id')
            serializer = self.get_serializer(queryset, many=True)
            return Utils.dispatch_success(request, serializer.data)
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def post(self, request, *args, **kwargs):
        """
        Creates a new user
        """
        try:
            self.serializer_class = CreateUserSerializer
            serializer = CreateUserSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Utils.dispatch_success(request, serializer.data)
            return Utils.dispatch_failure(request, 'VALIDATION_ERROR', serializer.errors)
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class UserDetail(views.APIView):
    """
    Retrieve, update or delete a User instance
    """
    permission_classes = (IsAuthenticatedOrCreate,)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Gets the Detail of a user by their ID
        """
        try:
            is_valid_user, contact_message = Utils.check_user_exists(pk)
            if not is_valid_user:
                return Utils.dispatch_failure(request, contact_message)

            user = self.get_object(pk)
            if self.request.user.is_superuser or request.user == user:
                user = self.get_object(pk)
                serializer = UserSerializer(user, context={'request': request})
                return Utils.dispatch_success(request, serializer.data)
            return Utils.dispatch_failure(request, 'UNAUTHORIZED_ACCESS')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def put(self, request, pk, format=None):
        """
        Updates the user by their ID
        """
        try:
            is_valid_user, contact_message = Utils.check_user_exists(pk)
            if not is_valid_user:
                return Utils.dispatch_failure(request, contact_message)

            user = self.get_object(pk)
            if request.user == user or request.user.is_superuser:
                serializer = UserSerializer(user, data=request.data, partial=True, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Utils.dispatch_success(request, serializer.data)

                return Utils.dispatch_failure(request, 'VALIDATION_ERROR', serializer.errors)

            return Utils.dispatch_failure(request, 'UNAUTHORIZED_ACCESS')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def delete(self, request, pk, format=None):
        """
        Deletes the user by their ID
        """
        try:
            is_valid_user, contact_message = Utils.check_user_exists(pk)
            if not is_valid_user:
                return Utils.dispatch_failure(request, contact_message)

            if self.request.user.is_superuser:
                user = self.get_object(pk)
                user.delete()
                return Utils.dispatch_success(request, 'DELETED_SUCCESSFULLY')
            return Utils.dispatch_failure(request, 'UNAUTHORIZED_ACCESS')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class CompanyList(generics.ListCreateAPIView):
    """
    Lists all companies
    """
    serializer_class = CompanySerializer
    # queryset = Company.objects.all ().order_by ('id')
    pagination_class = PageNumberPaginationDataOnly

    filter_backends = (DjangoFilterBackend,)
    filter_class = CompanyFilter
    search_fields = ('name',)

    def get(self, request, *args, **kwargs):
        try:
            queryset = Company.objects.all().order_by('id')
            serializer = self.get_serializer(queryset, many=True)
            return Utils.dispatch_success(request, serializer.data)
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def post(self, request, *args, **kwargs):
        """
        Creates a new company
        """
        try:
            serializer = CompanySerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Utils.dispatch_success(request, serializer.data)
            return Utils.dispatch_failure(request, 'VALIDATION_ERROR', serializer.errors)
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class CompanyDetail(views.APIView):
    """
    Retrieve, update or delete a Company instance
    """

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Gets a Company instance by ID
        """
        try:
            company = self.get_object(pk)
            serializer = CompanySerializer(company, context={'request': request})
            return Utils.dispatch_success(request, serializer.data)
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def put(self, request, pk, format=None):
        """
        Updates a Company instance by ID
        """
        try:
            company = self.get_object(pk)
            if self.request.user.is_superuser or self.request.user.company.id == int(pk):
                serializer = CompanySerializer(company, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Utils.dispatch_success(request, serializer.data)
                return Utils.dispatch_failure(request, 'VALIDATION_ERROR', serializer.errors)
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def delete(self, request, pk, format=None):
        """
        Deletes a Company instance by ID
        """
        try:
            if self.request.user.is_superuser:
                company = self.get_object(pk)
                company.delete()
                return Utils.dispatch_success(request, 'DELETED_SUCCESSFULLY')
            return Utils.dispatch_failure(request, 'UNAUTHORIZED_ACCESS')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class CompanyMetaDetail(views.APIView):
    """
    Retrieve, Update a Company's Metadata
    """

    def get_object(self, pk, request):
        try:
            return CompanyMeta.objects.get(company=pk)
        except Exception as e:
            return Utils.dispatch_failure(request, 'OBJECT_RESOURCE_NOT_FOUND')

    def get(self, request, pk, format=None):
        """
        Gets a Company Metadata instance by Company ID
        """
        try:
            company_meta = self.get_object(pk, request)
            serializer = CompanyMetaSerializer(company_meta, context={'request', request})
            return Utils.dispatch_success(request, serializer.data)
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def put(self, request, pk, format=None):
        """
        Updates a Company Metadata instance by Company ID
        """
        try:
            company_meta = self.get_object(pk, request)
            serializer = CompanyMetaSerializer(company_meta, data=request.data, context={'request', request},
                                               partial=True)
            if serializer.is_valid():
                serializer.save()
                return Utils.dispatch_success(request, serializer.data)
            return Utils.dispatch_failure(request, 'VALIDATION_ERROR', serializer.errors)
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    '''def post(self, request, pk, format=None):
        """
        Creates a Company Metadata instance by Company ID
        """
         try:
            company_meta = self.get_object(pk)
            serializer = CompanyMetaSerializer(company_meta, data=request.data, context={'request', request}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Utils.dispatch_success (request,serializer.data)
            return Utils.dispatch_failure(request,'VALIDATION_ERROR', serializer.errors)
        except Exception as e:
            return Utils.dispatch_failure (request,'INTERNAL_SERVER_ERROR')'''


# todo: need to indicate if user logging in is espresso admin or borrower
class LoginView(views.APIView):
    """
    Logs in the user with a post request
    """
    # TODO: Delete all previous
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        try:
            validate_user = LoginSerializer(data=request.data)
            if validate_user.is_valid():
                user = validate_user.validated_data
                print("---LOGGING IN--")
                user.last_login = timezone.now()
                user.is_logged_in = True
                user.save()
                serializer = UserLoginSerializer(user, context={'request': request})
                data = serializer.data
                if UserSession.objects.filter(user=user).count():
                    UserSession.objects.filter(user=user).delete()
                if data["company"] is None:
                    return Utils.dispatch_failure(request, "USER_NOT_CONNECTED")
                now = datetime.datetime.utcnow().replace(tzinfo=utc)
                UserSession.objects.create(user = user,start_time = now,end_time = now + datetime.timedelta(minutes=SESSION_EXPIRE_MINUTES))
                data ['session_expiry_timeout'] = SESSION_EXPIRE_MINUTES
                return Utils.dispatch_success(request,data)
            else:
                return Utils.dispatch_failure(request, "UNAUTHORIZED_ACCESS")
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

class LogoutView(views.APIView):
    """
    Logout  the user
    """
    permission_classes = (AllowAny,)
    def get(self, request):
        print(request.user)
        user=User.objects.filter(username=request.user).first()
        if user:
            user.is_logged_in = False
            user.save()
        return Utils.dispatch_success(request, [])

class Me(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        Returns the data of the user making the request
        """
        try:
            serializer = UserSerializer(self.request.user, context={'request': request})

            try:
                return Utils.dispatch_success(request, serializer.data)
            except Exception as e:
                Utils.send_company_meta(request.user,"META")
                return Utils.dispatch_failure(request, 'COMPANY_META_NOT_AVAILABLE')

        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class ContactDetails(views.APIView):
    """
    Retrieve, update or delete a Company instance
    """

    # serializer_class = ContactSerializer
    # pagination_class = PageNumberPaginationDataOnly
    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk, cid):
        try:
            return Contact.objects.get(company=pk, id=cid)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, cid=None):
        try:
            is_valid_contact, contact_message = Utils.check_contact_exists(pk, cid)
            if not is_valid_contact and cid is not None:
                return Utils.dispatch_failure(request, contact_message)

            if cid is not None:
                queryset = Contact.objects.filter(id=cid)
            else:
                queryset = Contact.objects.filter(company=pk)
            if queryset:
                serializer = ContactSerializer(queryset, many=True)
                return Utils.dispatch_success(request, serializer.data)
            return Utils.dispatch_success(request, 'DATA_NOT_FOUND')

        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def post(self, request, pk):
        """
        Creates a new User
        """
        try:
            data = request.data
            data['company'] = pk

            serializer = ContactSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Utils.dispatch_success(request, serializer.data)
            return Utils.dispatch_failure(request, 'VALIDATION_ERROR', serializer.errors)
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def put(self, request, pk, cid=None):
        """
        Updates a Company instance by ID and contact Id
        """
        try:
            is_valid_contact, contact_message = Utils.check_contact_exists(pk, cid)
            if not is_valid_contact and cid is not None:
                return Utils.dispatch_failure(request, contact_message)

            if cid is not None:
                contact = self.get_object(pk, cid)
                serializer = ContactSerializer(contact, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Utils.dispatch_success(request, serializer.data)
                return Utils.dispatch_failure(request, 'VALIDATION_ERROR', serializer.errors)

        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def delete(self, request, pk, cid=None):
        """
        Deletes a Company instance by ID
        """
        try:
            if self.request.user.is_superuser:
                is_valid_contact, contact_message = Utils.check_contact_exists(pk, cid)
                if not is_valid_contact and cid is not None:
                    return Utils.dispatch_failure(request, contact_message)

                if cid is not None:
                    contact = self.get_object(pk, cid)
                    contact.delete()
                    return Utils.dispatch_success(request, 'DELETED_SUCCESSFULLY')
                return Utils.dispatch_failure(request, "OBJECT_RESOURCE_NOT_FOUND")
            return Utils.dispatch_failure(request, 'UNAUTHORIZED_ACCESS')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class EspressoContacts(views.APIView):
    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk, cid=None):
        try:
            return EspressoContact.objects.get(company=pk, contact=cid)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, cid=None):
        try:
            is_valid_contact, contact_message = Utils.check_espressocontact_exists(pk, cid)
            if not is_valid_contact and cid is not None:
                return Utils.dispatch_failure(request, contact_message)

            queryset = {}
            if cid is not None:
                queryset = Contact.objects.filter(id=cid)
                queryset = [queryset[0]]
            else:
                contact_list = EspressoContact.objects.filter(company=pk).values('contact')
                if len(contact_list) > 0:
                    contact_ids = [val["contact"] for val in contact_list]
                    if len(contact_ids) > 0:
                        # Turn list of values into one big Q objects
                        query = reduce(lambda q, value: q | Q(pk=value), contact_ids, Q())
                        queryset = Contact.objects.filter(query)
            if queryset:
                serializer = ContactSerializer(queryset, many=True)
                return Utils.dispatch_success(request, serializer.data)
            return Utils.dispatch_success(request, 'DATA_NOT_FOUND')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def post(self, request, pk, *args, **kwargs):
        try:
            data_list = request.data
            data = {}
            if "contacts" not in data_list:
                return Utils.dispatch_failure(request, 'MISSING_PARAMETERS')
            contact_list = data_list["contacts"]
            contacts = {}
            c_count = 0
            for contact_id in contact_list:
                is_contact_exists = Contact.objects.filter(id=contact_id).count()
                if is_contact_exists == 0:
                    continue
                is_eccontact_exists = EspressoContact.objects.filter(contact=contact_id, company=pk).count()
                if is_eccontact_exists > 0:
                    continue
                data['contact'] = contact_id
                data['company'] = pk
                serializer = EspressoContactSerializer(data=data, context={'request': request})

                if serializer.is_valid():
                    serializer.save()
                    contacts[c_count] = serializer.data
                    c_count += c_count
                else:
                    return Utils.dispatch_failure(request, 'VALIDATION_ERROR', serializer.errors)
            if contacts:
                return Utils.dispatch_success(request, contacts)
            return Utils.dispatch_success(request, "DATA_NOT_FOUND")
                # else:
                #    return Utils.dispatch_failure(request,'VALIDATION_ERROR', {"Contact":"Contact does not exists" })
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def delete(self, request, pk, cid=None):
        try:
            if self.request.user.is_superuser:
                is_valid_contact, contact_message = Utils.check_espressocontact_exists(pk, cid)
                if not is_valid_contact:
                    return Utils.dispatch_failure(request, contact_message)

                if cid is not None:
                    contact = self.get_object(pk, cid)
                    contact.delete()
                    return Utils.dispatch_success(request, 'DELETED_SUCCESSFULLY')
                return Utils.dispatch_failure(request, "OBJECT_RESOURCE_NOT_FOUND")
            return Utils.dispatch_failure(request, 'UNAUTHORIZED_ACCESS')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class EmailValidation(generics.ListCreateAPIView):
    """
    Forgot Password Handler
    """
    permission_classes = (AllowAny,)
    serializer_class = ForgotPasswordValidationSerializer

    def post(self, request, *args, **kwargs):

        try:
            email = request.data.get("email")

            # Check if email parameter is on request
            if "email" not in request.data:
                return Utils.dispatch_failure(request, "RESOURCE_NOT_FOUND")

            # Check if email is valid
            if not Utils.validate_email_address(email):
                return Utils.dispatch_failure(request, "VALIDATION_ERROR")


            # Check if email is registered
            user = User.objects.filter(email=email)
            if not user:
                return Utils.dispatch_failure(request, "EMAIL_NOT_FOUND")
            if user.count() > 1:
                return Utils.dispatch_failure(request,"MULTIPLE_EMAIL_FOUND")

            # Generate unique token
            token = Utils.generate_unique_token()
            print(token)
            user = user.first()
            # Save forgot password details in table
            forgot_password = ForgotPasswordRequest(user=user, email=email, token=token,
                                                    request_time=datetime.datetime.utcnow().replace(tzinfo=utc),
                                                    expiry_time=int(30))
            forgot_password.save()

            subject = APP_NAME
            body = "Hi " + user.username.title() + ",\n\n"+FORGOT_PASSWORD_EMAIL_BODY+FORGOT_PASSWORD_EMAIL_URL + str(token) + "/\n"
            print(body)
            Utils.send_mail([email, ], subject=subject, body=body)

        except MultipleObjectsReturned:
            return Utils.dispatch_success(request, "EMAIL_SEND")
        except Exception:
            return Utils.dispatch_success(request, "EMAIL_SEND")


        return Utils.dispatch_success(request, "EMAIL_SEND")


class ForgotPassword(generics.ListCreateAPIView):
    """
    Forgot Password Handler
    """
    permission_classes = (AllowAny,)
    serializer_class = ForgotPasswordSerializer

    def get(self, request, token, *args, **kwargs):
        try:
            forgot_password_request = ForgotPasswordRequest.objects.get(token=token)
            request_time = forgot_password_request.request_time
            expiry_time_min = forgot_password_request.expiry_time
            current_time = datetime.datetime.utcnow().replace(tzinfo=utc)
            expiry_time = request_time + datetime.timedelta(minutes=expiry_time_min)
            if expiry_time >= current_time and not forgot_password_request.is_expired:
                return Utils.dispatch_success(request, "TOKEN_VALID")
            else:
                return Utils.dispatch_failure(request, "TOKEN_EXPIRED")
        except ForgotPasswordRequest.DoesNotExist:
            return Utils.dispatch_failure(request, "TOKEN_EXPIRED")

    def post(self, request, token, *args, **kwargs):
        try:
            forgot_password_request = ForgotPasswordRequest.objects.get(token=token)
            user = forgot_password_request.user
            password = request.data.get("password")
            reenter_password = request.data.get("reenter_password")

            if password == reenter_password:
                u = User.objects.get(username=str(user))
                u.set_password(password)
                u.save()
                forgot_password_request.is_expired = True
                forgot_password_request.save()
                # update_session_auth_hash(request, user)
            else:
                return Utils.dispatch_failure(request, "VALIDATION_ERROR")
        except MultipleObjectsReturned:
            return Utils.dispatch_failure(request, "TOKEN_EXPIRED")
        except ForgotPasswordRequest.DoesNotExist:
            return Utils.dispatch_failure(request, "TOKEN_EXPIRED")

        return Utils.dispatch_success(request, "PASSWORD_RESET_SUCCESSFUL")

class ChangePassword(views.APIView):
    """
    Forgot Password Handler
    """
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        try:
            user = request.data.get("id")
            passcode = request.data.get("passcode")
            password = passcode.get("password")
            reenter_password = passcode.get("reenter_password")

            if password == reenter_password:
                u = User.objects.get(id=user)
                u.set_password(password)
                u.is_password_reset = False
                u.save()
                return Utils.dispatch_success(request, "PASSWORD_RESET_SUCCESSFUL")
            else:
                return Utils.dispatch_failure(request, "VALIDATION_ERROR")
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class ScheduledMaintenanceDetails(views.APIView):
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs):
        try:
            response = {
                "is_under_maintenance": False,
            }
            maintenance = ScheduledMaintenance.objects.all().first()
            if maintenance and maintenance.is_active:
                now = datetime.datetime.utcnow().replace(tzinfo=utc)
                if maintenance.start_time < now < maintenance.end_time:
                    response["is_under_maintenance"] = maintenance.is_active
                    response["message"] = maintenance.message,
                    response["end_time"] = maintenance.end_time
                else:
                    maintenance.is_active = False
                    maintenance.save()
            return Utils.dispatch_success(request,response)
        except Exception:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

class TwoFactorAuthenticationDetails(views.APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        """
        Gets TOTP Secret Key for a user
        """
        try:
            user = User.objects.get(username=request.user)
            if user.tfa_secret_code is None:
                key = pyotp.random_base32()
                user.tfa_secret_code = key
                user.save()
            data = {
                "secret_code" : user.tfa_secret_code
            }
            return Utils.dispatch_success(request,data)
        except Exception as e:
            print(e)
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def post(self,request):
        """
        Check weather the totp is valid or not
        """
        try:
            user = User.objects.get(username=request.user)
            user_totp = request.data["code"]
            totp = pyotp.TOTP(user.tfa_secret_code)
            if int(user_totp) == int(totp.now()):
                return Utils.dispatch_success(request, [])
            else:
                return Utils.dispatch_failure(request,"VALIDATION_ERROR")
        except Exception as e:
            print(e)
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def put(self, request):
        """
        Updates Two factor flag
        """
        try:
            user = User.objects.get(username=request.user)
            is_tfa_enaled = request.data.get("is_tfa_enabled",None)
            is_tfa_setup_completed = request.data.get("is_tfa_setup_completed",None)
            if is_tfa_enaled is not None:
                user.is_tfa_enabled = is_tfa_enaled
            if is_tfa_setup_completed is not None:
                user.is_tfa_setup_completed = is_tfa_setup_completed
            user.save()
            return Utils.dispatch_success(request, [])
        except Exception as e:
            print(e)
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')
