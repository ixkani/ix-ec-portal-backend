import os
import datetime

from dateutil.relativedelta import relativedelta

from django.http import Http404
from django.utils import timezone
from django.core import serializers
from django.db.models import Q

from rest_framework import generics
from rest_framework import status
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from portalbackend.lendapi.reporting.models import MonthlyReport, Question, Answer,FinancialStatementEntry
from portalbackend.lendapi.utils import PageNumberPaginationDataOnly
from .serializers import MonthlyReportSerializer, CondensedMonthlyReportSerializer, QuestionWithAnswerSerializer, \
    CreateAnswerSerializer
from portalbackend.lendapi.reporting.utils import ReportingUtils
from portalbackend.lendapi.accounts.utils import AccountsUtils
from portalbackend.lendapi.accounting.models import CoAMap,FinancialStatementEntryTag
from portalbackend.lendapi.accounts.models import CompanyMeta,FiscalYearEnd
from portalbackend.validator.errormapping import ErrorMessage
from portalbackend.lendapi.v1.accounting.utils import Utils


class MonthlyReportList(generics.ListCreateAPIView):
    """
    Lists all Monthly Reports, or creates a new Monthly Report
    """
    serializer_class = MonthlyReportSerializer
    pagination_class = PageNumberPaginationDataOnly
    #permission_classes = (IsAuthenticated, )

    def get(self, request, pk, *args, **kwargs):
        """
        Lists all monthly reports for the specified companies
        """
        try:
            self.queryset = MonthlyReport.objects.filter(company=pk).order_by('period_ending')

            if len (self.queryset) == 0:
                return Utils.dispatch_success(request,'DATA_NOT_FOUND')
            return super(MonthlyReportList, self).get(request)
        except Exception:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


    def post(self, request, pk, *args, **kwargs):
        """
        Starts a new monthly report for the current reporting period, and moves next period ahead by 1 month to prepare
        for the next time. Will not create one that already exists, or create another one until the previous one
        is completed, this is a business rule.
        """
        try:
            company = AccountsUtils.get_company(pk)
            response_status = status.HTTP_200_OK
            response = ''

            meta = CompanyMeta.objects.filter(company_id=pk).first()
            current_period = meta.monthly_reporting_current_period
            next_period = meta.monthly_reporting_next_period

            if current_period is None:
                Utils.send_company_meta(request.user,"PERIOD")
                return Utils.dispatch_failure(request,'MISSING_MONTHLY_REPORTING_CURRENT_PERIOD')

            try:
                # does one exist for the current period
                report = MonthlyReport.objects.filter(company=company, period_ending=current_period).first()
                print('######## CURR AND NEXT - start as: c: ', current_period, ' n: ', next_period, ' rpt: ', report)
            except Exception as e:
                error = ["%s" % e]
                return Utils.dispatch_failure (request,'DATA_PARSING_ISSUE', error)


            # if it doesn't exist, or if the previous one has been completed, then it's ok to create a new one
            if not report or report.status == 'Complete':
                # todo: Due date is not relevant, remove it. We allow them to report any time after the end of the current
                # during initial setup, we do not advance the reporting dates. There is no initial setup for Form Entry
                # aka manual reporting
                if not meta.is_initial_setup:
                    print('#### moving period forward for new monthly report')
                    current_period = next_period
                    next_period = next_period + relativedelta(months=+1, day=31)
                    meta.monthly_reporting_current_period = current_period
                    meta.monthly_reporting_next_period = next_period
                    meta.monthly_reporting_current_period_status = 'IN_PROGRESS'
                    meta.save()
                    print('######## CURR AND NEXT - not initial setup, after move forward ', current_period, next_period)

                print('#### creating new monthly report for current period = ', meta.monthly_reporting_current_period)
                report = MonthlyReport(status='In Progress', company_id=pk, period_ending=current_period)
                report.save()

                response = serializers.serialize('json', [report, ])
                # return response
                return Utils.dispatch_success(request,[response])
            else:
                # was using HTTP_304_NOT_MODIFIED, but when this status is returned the JSON message is null which causes
                # problems for the UI
                # 409 causes the UI to stop processing because it thinks theres an error, but there isn't one.
                # so changing to 200 OK instead since it's OK to move forward
                # response_status = status.HTTP_409_CONFLICT
                return Utils.dispatch_success(request,'MONTHLY_REPORT_ALREADY_EXISTS_WITH_INPROGRESS')

        except Exception as e:
            return Utils.dispatch_failure (request,'INTERNAL_SERVER_ERROR')


class MonthlyReportDetail(views.APIView):

    def get(self, request, pk, report_identifier, *args, **kwargs):
        """
        Gets a Company's Monthly Report instance by Monthly Report Period or Monthly Report ID
        """
        try:
            if '-' in report_identifier:
                monthly_report = ReportingUtils.get_monthly_report(pk=pk, period=report_identifier)
            else:
                monthly_report = ReportingUtils.get_monthly_report(pk=pk, report_id=report_identifier)

            if monthly_report:
                serializer = MonthlyReportSerializer(monthly_report, context={'request': request, 'company_id': pk})
                return Utils.dispatch_success(request,serializer.data)
            return Utils.dispatch_success(request,'MONTHLY_REPORT_NOT_FOUND')
        except Exception as e:
            return Utils.dispatch_failure (request,'INTERNAL_SERVER_ERROR')


    def put(self, request, pk, report_identifier, *args, **kwargs):
        """
        Updates a Company's Monthly Report instance Monthly Report Period or Monthly Report ID
        """
        try:
            company = AccountsUtils.get_company(pk)
            if '-' in report_identifier:
                monthly_report = ReportingUtils.get_monthly_report(pk=pk, period=report_identifier)
            else:
                monthly_report = ReportingUtils.get_monthly_report(pk=pk, report_id=report_identifier)
            response_status = status.HTTP_200_OK  # default to OK and override if not

            if monthly_report:
                data = request.data
                data['company'] = company.id
                serializer = MonthlyReportSerializer(monthly_report, data=data,
                                                     context={'request': request, 'company_id': pk}, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Utils.dispatch_success(request,serializer.data)
                else:
                    return Utils.dispatch_failure (request,'VALIDATION_ERROR',serializer.errors)

            return Utils.dispatch_success (request,'MONTHLY_REPORT_NOT_FOUND')
        except Exception as e:
            return Utils.dispatch_failure (request,'INTERNAL_SERVER_ERROR')

    def delete(self, request,pk, report_identifier, *args, **kwargs):
        """
        Updates a Company's Monthly Report instance Monthly Report Period or Monthly Report ID
        """
        try:
            # TODO: Can you delete monthly reports? pls confirm
            if self.request.user.is_superuser:
                if '-' in report_identifier:
                    monthly_report = ReportingUtils.get_monthly_report(pk=pk, period=report_identifier)
                else:
                    monthly_report = ReportingUtils.get_monthly_report(pk=pk, report_id=report_identifier)
                if monthly_report:
                    monthly_report.delete()
                    return Utils.dispatch_success(request,'DELETED_SUCCESSFULLY')
                return Utils.dispatch_success(request, 'MONTHLY_REPORT_NOT_FOUND')
            return Utils.dispatch_failure(request,'UNAUTHORIZED_ACCESS')

        except Exception as e:
            return Utils.dispatch_failure (request,'INTERNAL_SERVER_ERROR')


class MonthlyReportStatusDetail(views.APIView):
    """
    Gets the status of the monthly report for that period and that company
    """

    def get(self, request, pk, report_identifier, *args, **kwargs):
        """
        Gets a Company's Monthly Report Status by Company ID and Monthly Report Period or Monthly Report ID
        """
        try:
            if '-' in report_identifier:
                monthly_report = ReportingUtils.get_monthly_report(pk=pk, period=report_identifier)
            else:
                monthly_report = ReportingUtils.get_monthly_report(pk=pk, report_id=report_identifier)
            serializer = CondensedMonthlyReportSerializer(monthly_report, context={'request': request, 'company_id': pk})
            if len(serializer.data) > 0:
                return Utils.dispatch_success (request,serializer.data)
            return Utils.dispatch_success (request,'MONTHLY_REPORT_NOT_FOUND')
        except Exception as e:
            return Utils.dispatch_failure (request,'INTERNAL_SERVER_ERROR')


class MonthlyReportSignoff(views.APIView):
    """
    Signs off on the status of the monthly report
    """
    def mark_coamap_verified(self,request, pk):
        """
        The verified flag on the CoAMap will remain false until the reporting period is signed off on
        so that the mapping exercise can be re-done easily at any point during the period.
        :return:
        """
        try:
            coamap = CoAMap.objects.filter(company_id=pk)
            for entry in coamap:
                # print('############# verified by = true')
                entry.verified_by_user = True
                # print('################ entry.verified_by_user ', entry.verified_by_user)
                entry.save()
        except Exception as e:
            return Utils.dispatch_failure (request,'INTERNAL_SERVER_ERROR')

    def put(self, request, pk, *args, **kwargs):

        try:
            company = AccountsUtils.get_company(pk)
            meta = CompanyMeta.objects.filter(company_id=pk).first()

            # get report for current period
            monthly_report = MonthlyReport.objects.filter(company_id=pk,
                                                          period_ending=meta.monthly_reporting_current_period).first()
            if monthly_report is None:
                return Utils.dispatch_failure(request, 'MONTHLY_REPORT_NOT_FOUND')

            if monthly_report.status == MonthlyReport.COMPLETE:
                #return Response({"status": "INFO", "message": ""})
                return Utils.dispatch_success(request,'MONTHLY_REPORT_ALREADY_EXISTS_WITH_COMPLETED')
            # if we're signing off as part of the setup process, then we need to set this flag to False
            # so the system will carry forward into it's normal monthly reporting workflow
            if meta.is_initial_setup:
                meta.qb_desktop_installed = True
                meta.is_initial_setup = False
                meta.accounting_setup_status = 'COMPLETE'

            meta.monthly_reporting_current_period_status = 'COMPLETE'
            meta.save()

            # todo: signoff_date and submitted_on date are duplicates at the moment, confirm with the business that we can
            #       conslidate and then merge these two fields. Submitting a report and signing off happen via the same
            #       UI activity.
            try:
                # checking next reporting period has fye. If not automatically new fye created with label
                # new "year_end fye" and mark it as active one
                cur_fye = FiscalYearEnd.objects.filter(company=company, is_active=True).first()
                if cur_fye is not None and  meta.monthly_reporting_next_period > cur_fye.fye_end_date:
                    cur_fye.is_active = False
                    cur_fye.save()
                    new_fye = FiscalYearEnd(company=company,
                                            fye_start_date=cur_fye.fye_start_date + relativedelta(years=1),
                                            fye_end_date=cur_fye.fye_end_date + relativedelta(years=1),
                                            label="{}FY".format((cur_fye.fye_end_date + relativedelta(years=1)).year),
                                            is_active=True)
                    new_fye.save()

                data = {
                    "status": MonthlyReport.COMPLETE,
                    "submitted_on": timezone.now().date(),
                    "signoff_date":  timezone.now().date(),
                    "signoff_by_name": request.data["signoff_by_name"],
                    "signoff_by_title": request.data["signoff_by_title"]
                }
            except Exception as e:
                error = ["%s" % e]
                return Utils.dispatch_failure(request,'DATA_PARSING_ISSUE', error)


            serializer = MonthlyReportSerializer(monthly_report, data=data,
                                                 context={'request': request, 'company_id': pk}, partial=True)

            # once they sign off on the current monthly reporting, the CoA Map entries will be officially verified
            # so they do not get asked to re-map them again the next time around
            MonthlyReportSignoff.mark_coamap_verified(self,request, pk)

            if serializer.is_valid():
                serializer.validated_data['company_id'] = pk
                serializer.save()
                return Utils.dispatch_success (request,serializer.data)
            return Utils.dispatch_failure(request,'VALIDATION_ERROR',serializer.errors)

        except Exception as e:
            return Utils.dispatch_failure (request,'INTERNAL_SERVER_ERROR')


class QuestionnaireList(views.APIView):

    def get(self, request, pk):
        """
        Gets a Company's Questionnaire answers
        """
        try:
            response = None
            response_status = status.HTTP_200_OK

            context = {'request': request,
                       'company': pk,
                       }

            # get an empty set of questions
            qs1 = Question.objects.filter(Q(common_to_all_companies=True, show_on_ui=True) |
                                          Q(common_to_all_companies=False, company=pk, show_on_ui=True))\
                                          .all()

            qs1 = ReportingUtils.sanitize_next_questions(qs1)

            serializer = QuestionWithAnswerSerializer(qs1, many=True, context=context)
            if len (serializer.data) > 0:
                return Utils.dispatch_success (request,serializer.data)
            return Utils.dispatch_success (request,'NO_ANSWER_FOUND')
        except Exception as e:
            return Utils.dispatch_failure(request,'INTERNAL_SERVER_ERROR')


class QuestionnaireDetail(views.APIView):

    def get(self, request, pk, report_identifier):
        """
        Gets a Company's Questionnaire answers for the requested period

        If called with no period specified, it simply returns a blank set of questions. The functionality supports
        the UI which dynamically displays the questions returned by the server.
        """
        try:
            response = None
            response_status = status.HTTP_200_OK

            context = {'request': request,
                       'company': pk,
                       'period': report_identifier}
            print('############### BEFORE INT COMPARISON')
            # todo: logic needs to be cleaned up. questions and has_answers have overlapping functionality that can be
            #       simplified

            questions = ReportingUtils.get_questionnaire_objects(pk, report_identifier)
            has_answers = ReportingUtils.has_answers_for_period(pk, report_identifier)

            if questions and has_answers:
                # return Q n A for requested period.
                serializer = QuestionWithAnswerSerializer(questions, many=True, context=context)
                if len(serializer.data) > 0:
                    return Utils.dispatch_success(request,serializer.data)
                return Utils.dispatch_success(request,'NO_ANSWER_FOUND')
            return Utils.dispatch_success (request, 'DATA_NOT_FOUND')
        except Exception as e:
            return Utils.dispatch_failure(request,'INTERNAL_SERVER_ERROR')


    def post(self, request, pk, report_identifier):
        """
        Updates or creates a Company's Questionnaire Answers for a given period
        """
        try:

            if '-' in report_identifier:
                monthly_report = ReportingUtils.get_monthly_report(pk=pk, period=report_identifier)
            else:
                monthly_report = ReportingUtils.get_monthly_report(pk=pk, report_id=report_identifier)

            if monthly_report is None:
                return Utils.dispatch_failure(request, 'MISSING_MONTHLY_REPORTING_PREVIOUS_PERIOD')

            answers = []
            context = {'request': request,
                       'company': pk,
                       'period': report_identifier}
            try:
                for item in request.data:
                    # None Values not checked becauseof, To update answer If yes, please provide details is changed to No scenario
                    # if item['answer'] is not None:
                    item['company'] = pk
                    item['monthly_report'] = monthly_report.id
                    exists = ReportingUtils.answer_exists(item)
                    if exists:
                        serializer = CreateAnswerSerializer(exists, data=item, context=context)
                    else:
                        serializer = CreateAnswerSerializer(data=item, context=context)
                    if serializer.is_valid():
                        serializer.save()
            except Exception as e:
                error = ["%s" % e]
                return Utils.dispatch_failure(request,'DATA_PARSING_ISSUE', error)
            questions = ReportingUtils.get_questionnaire_objects(pk, report_identifier)
            serializer = QuestionWithAnswerSerializer(questions, many=True, context=context)
            return Utils.dispatch_success(request,serializer.data)
        except Exception as e:
            return Utils.dispatch_failure (request,'INTERNAL_SERVER_ERROR')


class PreviousMonthlyReportEditDetails(views.APIView):
    def put(self, request, pk, report_identifier):
        try:
            company = AccountsUtils.get_company(pk)

            if '-' in report_identifier:
                monthly_report = ReportingUtils.get_monthly_report(pk=pk, period=report_identifier)
            else:
                monthly_report = ReportingUtils.get_monthly_report(pk=pk, report_id=report_identifier)

            changed_items = {
                "Balancesheet" : [],
                "Incomestatement" : [],
                "Answers" : [],
            }
            change_available = False
            data=request.data
            for name,value in data["Balancesheet"]["data"].items():
                if value is "":
                    value = "0.00"
                value = float (float (value.replace (',', '')))

                fse_tag = FinancialStatementEntryTag.objects.filter(all_sight_name = name).first()
                balancesheet = FinancialStatementEntry.objects.filter(company=company,
                                                                      period_ending=monthly_report.period_ending,
                                                                      statement_type=FinancialStatementEntry.BALANCE_SHEET,
                                                                      fse_tag =fse_tag
                                                                     ).first()

                if balancesheet is None:
                    continue

                if float(balancesheet.value) != float(value):
                    change_available = True
                    old_value = balancesheet.value
                    balancesheet.value = value
                    balancesheet.save()
                    changed_items["Balancesheet"].append({
                        "object":balancesheet,
                        "old_value":old_value,
                        "new_value":value
                    })

            for name,value in data["Incomestatement"]["data"].items():
                if value is "":
                    value = "0.00"
                value = float (float (value.replace (',', '')))

                fse_tag = FinancialStatementEntryTag.objects.filter(all_sight_name = name).first()
                incomestatement = FinancialStatementEntry.objects.filter(company=company,
                                                                      period_ending=monthly_report.period_ending,
                                                                      statement_type=FinancialStatementEntry.INCOME_STATEMENT,
                                                                      fse_tag =fse_tag
                                                                     ).first()
                if incomestatement is None:
                    continue

                if float(incomestatement.value) != float(value):
                    change_available = True
                    old_value = incomestatement.value
                    incomestatement.value = value
                    incomestatement.save()
                    changed_items["Incomestatement"].append({
                        "object": incomestatement,
                        "old_value": old_value,
                        "new_value": value
                    })

            for entry in data["Answers"]:
                answer_data = entry["answer"]
                answer_entry = Answer.objects.filter(id=answer_data["id"]).first()
                if str(answer_entry.answer) != str(answer_data["answer"]):
                    change_available = True
                    old_value = answer_entry.answer
                    answer_entry.answer = answer_data["answer"]
                    answer_entry.save()
                    changed_items["Answers"].append(
                        {
                            "object": answer_entry,
                            "old_value": old_value,
                            "new_value": answer_data["answer"]
                        }
                    )
            if change_available:
                Utils.log_prev_report_edit(company,monthly_report,request.user,changed_items)
            return Utils.dispatch_success(request,[])
        except Exception as e:
            print(e)
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')
