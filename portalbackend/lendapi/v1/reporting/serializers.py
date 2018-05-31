from portalbackend.lendapi.reporting.models import MonthlyReport, Question, Answer
from portalbackend.lendapi.accounts.models import Company
from rest_framework import serializers
from portalbackend.lendapi.v1.accounts.serializers import CompanySerializer
from portalbackend.validator.validator import init_validator_rules
from portalbackend.lendapi.reporting.utils import ReportingUtils

class MonthlyReportSerializer(serializers.ModelSerializer):
    # company = serializers.SerializerMethodField()

    # todo: remove me after testing to confirm I'm not needed any mmore
    # def get_company(self, obj):
    #     company_id = obj.company_id
    #
    #     if not company_id:
    #         company_id = self.context['company_id']
    #
    #     company = Company.objects.filter(id=company_id).first()
    #     serializer = CompanySerializer(company)
    #     return serializer.data

    class Meta:
        model = MonthlyReport
        fields = ('id', 'status', 'period_ending', 'due_date', 'submitted_on', 'lookup_period',
                  'signoff_by_name', 'signoff_by_title', 'signoff_date',)
        extra_kwargs = init_validator_rules(fields)


class CondensedMonthlyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyReport
        fields = ('id', 'status', 'period_ending', 'due_date', 'submitted_on')
        extra_kwargs = init_validator_rules(fields)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer')
        extra_kwargs = init_validator_rules(fields)


class CreateAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer', 'monthly_report', 'question', 'company')
        extra_kwargs = init_validator_rules(fields)


class NextQuestionSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()

    def get_answer(self, obj):
        period = self.context.get('period')
        company = self.context.get('company')

        report = MonthlyReport.objects.filter(lookup_period=period, company=company).first()
        if report:
            answer = Answer.objects.filter(company=company, monthly_report=report, question=obj.id).first()
            if not answer:
                return None
            return AnswerSerializer(answer).data

    class Meta:
        model = Question
        fields = [field.name for field in Question._meta.fields] + ['answer']
        extra_kwargs = init_validator_rules(fields)


class QuestionWithAnswerSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()
    next_question = NextQuestionSerializer()

    def get_answer(self, obj):
        period = self.context.get('period')
        company = self.context.get('company')

        report =  ReportingUtils.get_monthly_report(pk=company, period=period)

        # print('getting answers')
        if report:
            answer = Answer.objects.filter(company=company, monthly_report=report, question=obj.id).first()
            if not answer:
                return {"status": "SUCCESS", "message": "No answers found for "+period}
            return AnswerSerializer(answer).data

    class Meta:
        model = Question
        fields = [field.name for field in Question._meta.fields] + ['answer']
        extra_kwargs = init_validator_rules(fields)
