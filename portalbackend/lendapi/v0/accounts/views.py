from django.http import Http404
from rest_framework import generics
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from portalbackend.lendapi.accounts.models import Company, User, CompanyMeta

from .permissions import IsAuthenticatedOrCreate
from portalbackend.lendapi.utils import PageNumberPaginationDataOnly
from portalbackend.lendapi.v0.serializers import GenericSerializer


class UserList(generics.ListCreateAPIView):
    """
    Lists all users, or creates a new user
    """
    serializer_class = GenericSerializer

    def list(self, request, *args, **kwargs):
        data = [
            {
                "url": "http://127.0.0.1:8000/lend/v1/user/1/",
                "username": "gregmurray",
                "first_name": "greg",
                "last_name": "",
                "email": "gmurray@espressocapital.com",
                "company": {
                    "id": 3,
                    "name": "Developers",
                    "external_id": "X2003KDOWMXQ",
                    "default_currency": "CAD",
                    "website": "http://localhost.com",
                    "employee_count": 49,
                    "metadata": {
                        "reporting_connection_type": "Connections",
                        "last_reporting_period": "2017-08-08",
                        "qb_connect_desktop_version": "11.3",
                        "monthly_reporting_last_step": 2,
                        "qbo_auth_token": "SKM2003ASDL23"
                    }
                }
            },
            {
                "url": "http://127.0.0.1:8000/lend/v1/user/5/",
                "username": "mgenc",
                "first_name": "Mert",
                "last_name": "Genc",
                "email": "mgenc@espressocapital.com",
                "company": {
                    "id": 3,
                    "name": "Developers",
                    "external_id": "X2003KDOWMXQ",
                    "default_currency": "CAD",
                    "website": "http://localhost.com",
                    "employee_count": 49,
                    "metadata": {
                        "reporting_connection_type": "Connections",
                        "last_reporting_period": "2017-08-08",
                        "qb_connect_desktop_version": "11.3",
                        "monthly_reporting_last_step": 2,
                        "qbo_auth_token": "SKM2003ASDL23"
                    }
                }
            },
            {
                "url": "http://127.0.0.1:8000/lend/v1/user/7/",
                "username": "brad",
                "first_name": "Brad",
                "last_name": "Johnson",
                "email": "brad@espressocapital.com",
                "company": {
                    "id": 3,
                    "name": "Developers",
                    "external_id": "X2003KDOWMXQ",
                    "default_currency": "CAD",
                    "website": "http://localhost.com",
                    "employee_count": 49,
                    "metadata": {
                        "reporting_connection_type": "Connections",
                        "last_reporting_period": "2017-08-08",
                        "qb_connect_desktop_version": "11.3",
                        "monthly_reporting_last_step": 2,
                        "qbo_auth_token": "SKM2003ASDL23"
                    }
                }
            },
            {
                "url": "http://127.0.0.1:8000/lend/v1/user/8/",
                "username": "test2",
                "first_name": "test",
                "last_name": "lname",
                "email": "test@mail.io",
                "company": {
                    "id": 3,
                    "name": "Developers",
                    "external_id": "X2003KDOWMXQ",
                    "default_currency": "CAD",
                    "website": "http://localhost.com",
                    "employee_count": 49,
                    "metadata": {
                        "reporting_connection_type": "Connections",
                        "last_reporting_period": "2017-08-08",
                        "qb_connect_desktop_version": "11.3",
                        "monthly_reporting_last_step": 2,
                        "qbo_auth_token": "SKM2003ASDL23"
                    }
                }
            },
            {
                "url": "http://127.0.0.1:8000/lend/v1/user/9/",
                "username": "test3",
                "first_name": "fname",
                "last_name": "lname",
                "email": "mytest@mail.io",
                "company": {
                    "id": 3,
                    "name": "Developers",
                    "external_id": "X2003KDOWMXQ",
                    "default_currency": "CAD",
                    "website": "http://localhost.com",
                    "employee_count": 49,
                    "metadata": {
                        "reporting_connection_type": "Connections",
                        "last_reporting_period": "2017-08-08",
                        "qb_connect_desktop_version": "11.3",
                        "monthly_reporting_last_step": 2,
                        "qbo_auth_token": "SKM2003ASDL23"
                    }
                }
            }
        ]
        return Response(data=data)

    def post(self, request, *args, **kwargs):
        data = {
              "url": "http://127.0.0.1:8000/lend/v1/user/12/",
              "username": "testsignup",
              "first_name": "Test",
              "last_name": "User",
              "email": "user@fakemail.com",
              "company": 3
            }
        return Response(data=data)

    permission_classes = (IsAuthenticatedOrCreate, )


class UserDetail(views.APIView):
    """
    Retrieve, update or delete a User instance
    """
    def get(self, request, pk, format=None):
        data = {
              "url": "http://127.0.0.1:8000/lend/v1/user/1/",
              "username": "gregmurray",
              "first_name": "greg",
              "last_name": "",
              "email": "gmurray@espressocapital.com",
              "company": {
                "id": 3,
                "name": "Developers",
                "external_id": "X2003KDOWMXQ",
                "default_currency": "CAD",
                "website": "http://localhost.com",
                "employee_count": 49,
                "metadata": {
                  "reporting_connection_type": "Connections",
                  "last_reporting_period": "2017-08-08",
                  "qb_connect_desktop_version": "11.3",
                  "monthly_reporting_last_step": 2,
                  "qbo_auth_token": "SKM2003ASDL23"
                }
              }
            }
        return Response(data=data)

    def put(self, request, pk, format=None):
        data = {
          "url": "http://127.0.0.1:8000/lend/v1/user/1/",
          "username": "gregmurray",
          "first_name": "greg_update",
          "last_name": "",
          "email": "gmurray@espressocapital.com",
          "company": {
            "id": 3,
            "name": "Developers",
            "external_id": "X2003KDOWMXQ",
            "default_currency": "CAD",
            "website": "http://localhost.com",
            "employee_count": 49,
            "metadata": {
              "reporting_connection_type": "Connections",
              "last_reporting_period": "2017-08-08",
              "qb_connect_desktop_version": "11.3",
              "monthly_reporting_last_step": 2,
              "qbo_auth_token": "SKM2003ASDL23"
            }
          }
        }
        return Response(data=data)

    def delete(self, request, pk, format=None):
        return Response(status=status.HTTP_204_NO_CONTENT)


class CompanyList(generics.ListCreateAPIView):
    """
    Lists all companies, or creates a new company
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = GenericSerializer
    def list(self, request, *args, **kwargs):
        data = [
              {
                "id": 3,
                "name": "Developers",
                "external_id": "X2003KDOWMXQ",
                "default_currency": "CAD",
                "website": "http://localhost.com",
                "employee_count": 49,
                "metadata": {
                  "reporting_connection_type": "Connections",
                  "last_reporting_period": "2017-08-08",
                  "qb_connect_desktop_version": "11.3",
                  "monthly_reporting_last_step": 2,
                  "qbo_auth_token": "SKM2003ASDL23"
                }
              },
              {
                "id": 1,
                "name": "ABCCo REVISED",
                "external_id": "293002390001",
                "default_currency": "CAD",
                "website": "http://www.localhost.com",
                "employee_count": 77,
                "metadata": {
                  "reporting_connection_type": "Connections",
                  "last_reporting_period": "2017-08-08",
                  "qb_connect_desktop_version": "11.3",
                  "monthly_reporting_last_step": 3,
                  "qbo_auth_token": "5JSDN2EIXX"
                }
              }
            ]
        return Response(data=data)

    def post(self, request, *args, **kwargs):
        data = {
              "id": 4,
              "name": "new_comp",
              "external_id": "239XKSEMA",
              "default_currency": "CAD",
              "website": "http://localhost.com",
              "employee_count": 84,
              "metadata": {
                "reporting_connection_type": "",
                "last_reporting_period": None,
                "qb_connect_desktop_version": "",
                "monthly_reporting_last_step": None,
                "qbo_auth_token": ""
              }
            }
        return Response(data=data)


class CompanyDetail(views.APIView):
    """
    Retrieve, update or delete a Company instance
    """

    def get(self, request, pk, format=None):
        data = {
          "id": 4,
          "name": "new_comp",
          "external_id": "239XKSEMA",
          "default_currency": "CAD",
          "website": "http://localhost.com",
          "employee_count": 84,
          "metadata": {
            "reporting_connection_type": "",
            "last_reporting_period": None,
            "qb_connect_desktop_version": "",
            "monthly_reporting_last_step": None,
            "qbo_auth_token": ""
          }
        }
        return Response(data=data)

    def put(self, request, pk, format=None):
        data = {
          "id": 4,
          "name": "updated_comp",
          "external_id": "239XKSEMA",
          "default_currency": "CAD",
          "website": "http://localhost.com",
          "employee_count": 84,
          "metadata": {
            "reporting_connection_type": "",
            "last_reporting_period": None,
            "qb_connect_desktop_version": "",
            "monthly_reporting_last_step": None,
            "qbo_auth_token": ""
          }
        }
        return Response(data=data)

    def delete(self, request, pk, format=None):
        return Response(status=status.HTTP_204_NO_CONTENT)


class CompanyMetaDetail(views.APIView):
    """
    Retrieve, Update or delete a Company Metadata
    """
    def get(self, request, pk, format=None):
        data = {
          "reporting_connection_type": "Connections_updated",
          "last_reporting_period": "2017-08-08",
          "qb_connect_desktop_version": "11.3",
          "monthly_reporting_last_step": 2,
          "qbo_auth_token": "SKM2003ASDL23"
        }
        return Response(data)

    def put(self, request, pk, format=None):
        data = {
          "reporting_connection_type": "Connections_updated",
          "last_reporting_period": "2017-08-08",
          "qb_connect_desktop_version": "11.3",
          "monthly_reporting_last_step": 2,
          "qbo_auth_token": "SKM2003ASDL23"
        }
        return Response(data)

    def post(self, request, pk):
        data = {
              "reporting_connection_type": "Connections",
              "last_reporting_period": "2017-08-08",
              "qb_connect_desktop_version": "11.3",
              "monthly_reporting_last_step": 2,
              "qbo_auth_token": "SKM2003ASDL23"
            }
        return Response(data)


class LoginView(views.APIView):
    """
    Logs in the user with a post request, returns Auth Token
    """
    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        data = {
          "url": "http://127.0.0.1:8000/lend/v1/user/1/",
          "username": "gregmurray",
          "first_name": "greg_update",
          "last_name": "",
          "email": "gmurray@espressocapital.com",
          "company": {
            "id": 3,
            "name": "Developers",
            "external_id": "X2003KDOWMXQ",
            "default_currency": "CAD",
            "website": "http://localhost.com",
            "employee_count": 49,
            "metadata": {
              "reporting_connection_type": "Connections",
              "last_reporting_period": "2017-08-08",
              "qb_connect_desktop_version": "11.3",
              "monthly_reporting_last_step": 2,
              "qbo_auth_token": "SKM2003ASDL23"
            }
          }
        }
        return Response(data)
