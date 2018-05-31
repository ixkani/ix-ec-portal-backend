from rest_framework import serializers

from portalbackend.validator.validator import init_validator_rules
from portalbackend.lendapi.accounting.models import CoAMap, FinancialStatementEntryTag, TrialBalance, CoA, LoginInfo
from portalbackend.lendapi.accounts.models import Company
from portalbackend.lendapi.reporting.models import FinancialStatementEntry


class FinStatementTagSerializer(serializers.ModelSerializer):
    """
    Serializer handles the Financial Statement Entry Tag
    """
    class Meta:
        model = FinancialStatementEntryTag
        fields = ('name', 'description', 'tag_id', 'tag_category', 'tag_group', 'is_total_row', 'sort_order',
                  'all_sight_name','formula',)
        # Init validator rule
        extra_kwargs = init_validator_rules (fields)


class CoAMapSerializer(serializers.ModelSerializer):
    """
    The Serializer which returns the CoaMap with options of fields from the statement entry tags.
    Abstract tags are filtered out of the map by virtue of the defaultaccounttagmapping table, in which they do
    not exist and therefore will not make it into the mapping
    """
    mapping_options = serializers.SerializerMethodField()
    tag_group = serializers.SerializerMethodField()

    def get_mapping_options(self, obj):
        """
        Fetches Mapping options from the  database based on categories related to espresso account id
        :param obj:
        :return:
        """
        row = FinancialStatementEntryTag.objects.filter(tag_id=obj.espresso_account_id).first()
        if row:
            options = FinancialStatementEntryTag.objects.filter(tag_category=row.tag_category, abstract=False)
        else:
            options = ''
        return FinStatementTagSerializer(options, many=True).data

    def get_tag_group(self, obj):
        group = FinancialStatementEntryTag.objects.filter(tag_id=obj.espresso_account_id).first().tag_group
        return group

    class Meta:
        model = CoAMap
        fields = ('company', 'cust_account_id', 'cust_account_name', 'espresso_account_id', 'espresso_account_name',
                  'tag_group', 'mapping_options', 'is_mapped', 'verified_by_user')
        # Init validator rule
        extra_kwargs = init_validator_rules (fields)


class UpdatedCoAMapSerializer(serializers.ModelSerializer):
    """
    The Serializer Which returns the updated CoAMap
    """
    class Meta:
        model = CoAMap
        fields = ('company', 'cust_account_id', 'cust_account_name',
                  'espresso_account_id', 'espresso_account_name', 'verified_by_user')
        # Init validator rule
        extra_kwargs = init_validator_rules (fields)



class CoASerializer(serializers.ModelSerializer):
    """
    The Serializer which handles the Chart of Accounts
    """
    class Meta:
        model = CoA
        fields = ('company', 'gl_account_id', 'gl_account_name', 'gl_account_type', 'gl_account_bal'
                  , 'gl_account_currency')
        # Init validator rule
        extra_kwargs = init_validator_rules (fields)


class TrialBalanceSerializer(serializers.ModelSerializer):
    """
    The Serializer which handles the Trial Balance Objects
    """
    class Meta:
        model = TrialBalance
        fields = ('company', 'gl_account_name', 'gl_account_id', 'debit', 'credit', 'period', 'currency')
        # Init validator rule
        extra_kwargs = init_validator_rules (fields)


class FinancialStatementEntrySerializer(serializers.ModelSerializer):
    """
    The Serializer which handles financial statement entries, and also includes the financial statement entry tag
    """
    fse_tag = FinStatementTagSerializer()


    data = serializers.SerializerMethodField()

    def get_data(self,obj):
        ret = [{obj.fse_tag.all_sight_name : obj.value}]
        return ret[0]

    def value(self,obj):
        return int(obj.value)

    class Meta:
        model = FinancialStatementEntry

        fields = ('company', 'monthly_report', 'fse_tag', 'period_ending', 'value', 'currency', 'statement_type','data')
        # Init validator rule
        extra_kwargs = init_validator_rules (fields)




class LoginInfoSerializer(serializers.ModelSerializer):
    """
    The Serializer which handles status of Login
    """
    class Meta:
        model = LoginInfo
        fields = ('status',)


class CompanyDetailSerializer(serializers.ModelSerializer):
    """
        The Serializer which handles status of Company Profile
    """

    class Meta:
        model = Company
        fields = ('id', 'name', 'external_id', 'default_currency', 'website', 'employee_count', 'accounting_type')
        # Init validator rule
        extra_kwargs = init_validator_rules (fields)
