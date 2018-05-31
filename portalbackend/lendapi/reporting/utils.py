from django.http import Http404

from .models import Answer, MonthlyReport, Question
from django.db.models import Q
import calendar
import datetime
from django.utils import timezone
from dateutil import relativedelta


class ReportingUtils(object):
    @staticmethod
    def answer_exists(data):
        answer = Answer.objects.filter(company=data['company'],
                                       monthly_report=data['monthly_report'], question=data['question']).first()
        if answer:
            return answer
        return False

    @staticmethod
    def sanitize_next_questions(data):
        """
        Ensures that the return data does not contain the next questions, just the parent questions,
         with next questions included inside them
        :param data:
        :return:
        """
        next_questions = []
        questions = [question for question in data]
        for question in questions:
            if question.next_question:
                next_questions.append(question.next_question_id)

        sanitized = [question for question in questions if question.id not in next_questions]
        sanitized.sort(key=lambda x: x.ask_order)
        return sanitized

    @staticmethod
    def get_monthly_report(pk, period=None, report_id=None):

        # todo: using period variable as both period and id is not good. need to fix with named parameters or defaults

        if period:
            monthly_report = MonthlyReport.objects.filter(company_id=pk, lookup_period=period).first()
            # print('company_id is ', pk, ' and lookup period is ', period)
        else:
            monthly_report = MonthlyReport.objects.filter(company=pk, id=report_id).first()
            # print('company_id is ', pk, ' and lookup id is ', report_id)

        # print('mr is ', monthly_report)

        if not monthly_report:
            return None
        return monthly_report

    @staticmethod
    def has_answers_for_period(pk, report_identifier):
        has_answers = False
        # see if a report exists for the period

        if '-' in report_identifier:
            monthly_report = ReportingUtils.get_monthly_report(pk=pk, period=report_identifier)
        else:
            monthly_report = ReportingUtils.get_monthly_report(pk=pk, report_id=report_identifier)
        if monthly_report:
            # if it does, see if any answers exist for the period
            answers = Answer.objects.filter(company_id=pk, monthly_report_id=monthly_report.id)
            if answers:
                has_answers = True

        return has_answers

    # todo: this function can probably be removed and it's functionality replaced in QuestionnaireList class
    @staticmethod
    def get_questionnaire_objects(pk, report_identifier):
        if '-' in report_identifier:
            monthly_report = ReportingUtils.get_monthly_report(pk=pk, period=report_identifier)
        else:
            monthly_report = ReportingUtils.get_monthly_report(pk=pk, report_id=report_identifier)

        if monthly_report:
            qs1 = Question.objects.filter(common_to_all_companies=True, show_on_ui=True).all()
            qs2 = Question.objects.filter(common_to_all_companies=False,show_on_ui=True,company=pk).all()
            if not qs1 and qs2:
                qs2 = ReportingUtils.sanitize_next_questions(qs2)
                return qs2
            elif qs1 and not qs2:
                qs1 = ReportingUtils.sanitize_next_questions(qs1)
                return qs1
            elif qs1 and qs2:
                qs = ReportingUtils.sanitize_next_questions(qs1.union(qs2))
                return qs
            else:
                return None
        else:
            return None

    @staticmethod
    def monthly_reporting_complete(company, period):
        """
        Does not allow a company to create a new monthly report, if any previous reports are not complete
        """
        reports = MonthlyReport.objects.filter(~Q(status=MonthlyReport.COMPLETE), company=company,
                                               period_ending__lt=period)
        if reports:
            return {"message": "no monthly reports submitted for {}".format(
                ','.join([report.lookup_period for report in reports]))}

        return None

    @staticmethod
    def add_months(date, months):
        month = date.month - 1 + months
        year = int(date.year + month / 12)
        month = month % 12 + 1
        return datetime.date(year, month, calendar.monthrange(year, month)[1])

    @staticmethod
    def create_query_list(months=24):
        """
        Creates a list of querystrings for quickbooks, starting from current month - 1, then 24 months
        """
        end = timezone.now().date()
        end = end - relativedelta.relativedelta(months=1)
        start = end - relativedelta.relativedelta(months=months)
        curr_date = start
        date_list = []
        while curr_date < end:
            date_list.append(curr_date)
            curr_date += relativedelta.relativedelta(months=1)

        query_list = []
        for date in date_list:
            first = datetime.date(date.year, date.month, 1)
            last = datetime.date(date.year, date.month, calendar.monthrange(date.year, date.month)[1])
            query = '?start_date='+first.strftime('%Y-%m-%d')+'&end_date='+last.strftime('%Y-%m-%d')
            query_list.append(query)
        return query_list
