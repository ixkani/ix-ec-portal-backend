import json
import re

from rest_framework import permissions, status
from rest_framework.exceptions import APIException
from portalbackend.validator.errormapping import ErrorMessage
from portalbackend.validator.errorcodemapping import ErrorCode
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime, timedelta
from portalbackend.lendapi.accounts.models import UserSession
from re import sub
from oauth2_provider.models import AccessToken
from portalbackend.lendapi.v1.accounting.utils import Utils
from django.http import JsonResponse
from django.utils.timezone import utc
from portalbackend.lendapi.constants import SESSION_EXPIRE_MINUTES, SESSION_SAVE_URLS


class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super(IsAuthenticatedOrCreate, self).has_permission(request, view)


class ResourceNotFound(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {"message": ErrorMessage.RESOURCE_NOT_FOUND, "status": "failed"}


class UnauthorizedAccess(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = {"message": ErrorMessage.UNAUTHORIZED_ACCESS, "status": "failed"}


class IsCompanyUser(permissions.IsAuthenticated):
    message = {"message": ErrorMessage.UNAUTHORIZED_ACCESS, "status": "failed"}

    def has_permission(self, request, view):
        try:
            split_url = request.META.get('PATH_INFO').split("/")

            if split_url[3] == "docs":
                return request.user.is_authenticated()

            if len(view.kwargs) == 0 or split_url[3] != "company":
                if request.user.is_superuser:
                    return request.user and request.user.is_authenticated()
                else:
                    raise UnauthorizedAccess

            is_valid_company, message = Utils.check_company_exists(view.kwargs["pk"])
            if not is_valid_company:
                raise ResourceNotFound

            if request.user.is_superuser:
                return request.user and request.user.is_authenticated()
            else:

                return ((request.user.is_superuser or request.user.company.id == int(
                    view.kwargs["pk"])) and request.user.is_authenticated())

        except APIException as err:
            raise err


class SessionValidator(MiddlewareMixin):
    def process_request(self, request):
        try:
            session_save_urls = SESSION_SAVE_URLS
            request_api_url = request.META.get('PATH_INFO')
            for url in session_save_urls:
                if re.search(url, request_api_url):
                    return

            header_token = request.META.get('HTTP_AUTHORIZATION', None)
            if header_token is not None:
                token = sub('Token ', '', request.META.get('HTTP_AUTHORIZATION', None))
                token = token.split(' ')
                token_obj = AccessToken.objects.get(token=token[1])
                user = token_obj.user
                try:
                    user_session = UserSession.objects.get(user=user)
                    if user_session:
                        if user_session.is_first_time:
                            user_session.is_first_time = False
                            user_session.auth_key = token_obj

                        if user_session.auth_key == token_obj:
                            now = datetime.utcnow().replace(tzinfo=utc)
                            if user_session.end_time > now:
                                user_session.end_time = now + timedelta(minutes=SESSION_EXPIRE_MINUTES)
                                user_session.save()
                            else:
                                user_session.delete()
                                return JsonResponse(
                                    {'error': ErrorMessage.SESSION_EXPRIED, 'code': ErrorCode.SESSION_EXPRIED},
                                    status=401)
                        else:
                            return JsonResponse(
                                {'error': ErrorMessage.SESSION_ALREADY_ACTIVE,
                                 'code': ErrorCode.SESSION_ALREADY_ACTIVE},
                                status=401)

                except UserSession.DoesNotExist:
                    return JsonResponse({'error': ErrorMessage.SESSION_EXPRIED, 'code': ErrorCode.SESSION_EXPRIED},
                                        status=401)
        except Exception as e:
            print(e)

        return