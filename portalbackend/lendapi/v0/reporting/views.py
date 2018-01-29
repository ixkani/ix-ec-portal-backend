from django.http import Http404
from rest_framework import generics
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone

from portalbackend.lendapi.reporting.models import MonthlyReport, Question, Answer
from portalbackend.lendapi.utils import PageNumberPaginationDataOnly
from portalbackend.lendapi.v0.serializers import GenericSerializer

class MonthlyReportList(generics.ListCreateAPIView):
    """
    Lists all Monthly Reports, or creates a new Monthly Report
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = GenericSerializer

    def list(self, request, *args, **kwargs):
        data = [
            {
                "id": 2,
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
                },
                "status": "Complete",
                "period_ending": "2017-08-08",
                "due_date": "2017-08-08",
                "submitted_on": "2017-08-14",
                "lookup_period": "2017-08"
            },
            {
                "id": 7,
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
                },
                "status": "In Progress",
                "period_ending": "2017-08-08",
                "due_date": "2017-08-08",
                "submitted_on": None,
                "lookup_period": "2017-08"
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        data = {
            "id": 7,
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
            },
            "status": "In Progress",
            "period_ending": "2017-08-08",
            "due_date": "2017-08-08",
            "submitted_on": None,
            "lookup_period": "2017-08"
        }
        return Response(data)


class MonthlyReportDetail(views.APIView):
    """
    Retrieve, Update, or Delete a Companys Monthly Report
    """
    def get(self, request, pk, period, *args, **kwargs):
        data = {
            "id": 2,
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
            },
            "status": "Complete",
            "period_ending": "2017-08-08",
            "due_date": "2017-08-08",
            "submitted_on": "2017-08-14",
            "lookup_period": "2017-08"
        }
        return Response(data)

    def put(self, request, pk, period, *args, **kwargs):
        data = {
            "id": 2,
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
            },
            "status": "Complete",
            "period_ending": "2017-08-08",
            "due_date": "2017-08-08",
            "submitted_on": "2017-08-14",
            "lookup_period": "2017-08"
        }
        return Response(data)

    def delete(self, pk, period, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class MonthlyReportStatusDetail(views.APIView):
    """
    Gets the status of the monthly report for that period and that company
    """
    def get(self, request, pk, period, *args, **kwargs):
        data = {
            "id": 2,
            "status": "Complete",
            "period_ending": "2017-08-08",
            "due_date": "2017-08-08",
            "submitted_on": "2017-08-14"
        }
        return Response(data)


class MonthlyReportSignoff(views.APIView):
    """
    Signs off on the status of the monthly report
    """
    def post(self, request, pk, period, *args, **kwargs):
        data = {
            "id": 2,
            "status": "Complete",
            "period_ending": "2017-08-08",
            "due_date": "2017-08-08",
            "submitted_on": "2017-08-14"
        }
        return Response(data)

class QuestionnaireList(views.APIView):

    def get(self, request, pk, period):
        data = [
            {
                "id": 6,
                "company": 3,
                "next_question": {
                    "id": 7,
                    "company": 3,
                    "next_question": None,
                    "next_question_if": "",
                    "question_category": 1,
                    "question_text": "Could you explain why?",
                    "question_choices": [],
                    "short_tag": "Service Explanation",
                    "answer_data_type": "Text",
                    "answer_validation_regex": "",
                    "ask_order": 2,
                    "show_on_ui": True,
                    "common_to_all_companies": True,
                    "answer": None
                },
                "next_question_if": "Yes",
                "question_category": 1,
                "question_text": "Are you enjoy Espresso Services",
                "question_choices": [
                    "Yes",
                    "No"
                ],
                "short_tag": "Enjoying Services",
                "answer_data_type": "Text",
                "answer_validation_regex": "",
                "ask_order": 1,
                "show_on_ui": True,
                "common_to_all_companies": False,
                "answer": None
            },
            {
                "id": 8,
                "company": 3,
                "next_question": None,
                "next_question_if": "",
                "question_category": 1,
                "question_text": "This is the third question, filler text",
                "question_choices": [
                    "Option One",
                    "Option Two",
                    "Option Three",
                    "Option Four"
                ],
                "short_tag": "Third Question",
                "answer_data_type": "Text",
                "answer_validation_regex": "",
                "ask_order": 3,
                "show_on_ui": True,
                "common_to_all_companies": True,
                "answer": None
            }
        ]
        return Response(data)

    def post(self, request, pk, period):
        data = [
            {
                "id": 6,
                "company": 3,
                "next_question": {
                    "id": 7,
                    "company": 3,
                    "next_question": None,
                    "next_question_if": "",
                    "question_category": 1,
                    "question_text": "Could you explain why?",
                    "question_choices": [],
                    "short_tag": "Service Explanation",
                    "answer_data_type": "Text",
                    "answer_validation_regex": "",
                    "ask_order": 2,
                    "show_on_ui": True,
                    "common_to_all_companies": True,
                    "answer": {
                        "id": 8,
                        "answer": "I feel like they provide wonderful types of financing, love it, the best."
                    }
                },
                "next_question_if": "Yes",
                "question_category": 1,
                "question_text": "Are you enjoy Espresso Services",
                "question_choices": [
                    "Yes",
                    "No"
                ],
                "short_tag": "Enjoying Services",
                "answer_data_type": "Text",
                "answer_validation_regex": "",
                "ask_order": 1,
                "show_on_ui": True,
                "common_to_all_companies": True,
                "answer": {
                    "id": 7,
                    "answer": "Yes"
                }
            },
            {
                "id": 8,
                "company": 3,
                "next_question": None,
                "next_question_if": "",
                "question_category": 1,
                "question_text": "This is the third question, filler text",
                "question_choices": [
                    "Option One",
                    "Option Two",
                    "Option Three",
                    "Option Four"
                ],
                "short_tag": "Third Question",
                "answer_data_type": "Text",
                "answer_validation_regex": "",
                "ask_order": 3,
                "show_on_ui": True,
                "common_to_all_companies": True,
                "answer": {
                    "id": 9,
                    "answer": "Option Four"
                }
            }
        ]
        return Response(data)
