import os
from django.contrib.auth import authenticate
from django.http import HttpRequest
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from portalbackend.lendapi.accounts.models import Company, User, CompanyMeta, Contact, EspressoContact, \
    ForgotPasswordRequest

from portalbackend.validator.validator import init_validator_rules

class CompanyMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyMeta
        fields = ('monthly_reporting_sync_method', 'monthly_reporting_current_period',
                  'monthly_reporting_next_period', 'monthly_reporting_current_period_status',
                  'qb_connect_desktop_version', 'monthly_reporting_last_step',
                  'accounting_setup_status', 'last_page', 'is_initial_setup', 'trialbalance_dl_complete',
                  'qb_desktop_installed', 'chartofaccounts_last_refresh_date', 'trialbalance_last_refresh_date')

        # Init validator rule
        extra_kwargs = init_validator_rules(fields)


class CompanySerializer(serializers.ModelSerializer):
    metadata = serializers.SerializerMethodField()

    def get_metadata(self, obj):
        return CompanyMetaSerializer(CompanyMeta.objects.filter(company_id=obj.id).first()).data

    class Meta:
        model = Company
        fields = ('id', 'name', 'external_id', 'default_currency', 'website', 'employee_count', 'accounting_type',
                  'metadata')

        read_only_fields = ('meta_data', )

        # Init validator rule
        extra_kwargs = init_validator_rules(fields)


class UserSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    password = serializers.CharField(write_only=True)
    qbd_user_config = serializers.SerializerMethodField()

    # todo: we need to also send a JSON file with the configurations. Create a new function for send config
    def get_qbd_user_config(self, obj):

        user_data = User.objects.filter(id=obj.id).first()
        company_metadata = CompanyMeta.objects.filter(company=user_data.company_id).first()

        # print('User ', User.objects.filter(id=obj.id).values())
        # print('Meta ', CompanyMeta.objects.filter(company=user_data.company_id).values())

        base_url = HttpRequest.get_host(self.context.get('request'))

        # comes from heroku environment variables
        # todo: how are we going to get this locally?
        qbd_version = os.environ.get('QUICKBOOKS_DESKTOP_APP_VERSION')
        monitoring_redirect_page = os.environ.get('MONITORING_REDIRECT_PAGE')

        if not qbd_version:
            qbd_version = '0'

        # todo: need to add page for local development and testing
        if not monitoring_redirect_page:
            monitoring_redirect_page = '/nopage'

        if user_data.is_superuser:
            monthly_reporting_current_period = ""
            qb_connect_desktop_version = ""

        else:
            monthly_reporting_current_period = company_metadata.monthly_reporting_current_period
            qb_connect_desktop_version = company_metadata.qb_connect_desktop_version

        data = {
            "user_name": user_data.username,
            "base_url": base_url,
            "monitoring_redirect_url": base_url+monitoring_redirect_page,
            "current_report_date": monthly_reporting_current_period,
            "qb_desktop_company_version": qb_connect_desktop_version,
            "qb_desktop_current_version": qbd_version
        }
        return data

    class Meta:
        model = User
        fields = ('id', 'url', 'role', 'username', 'first_name', 'last_name', 'email', 'company'
                  , 'password', 'qbd_user_config','enforce_tfa_enabled','is_tfa_enabled','is_tfa_setup_completed','tour_guide_enabled')

        # Init validator rule
        extra_kwargs = init_validator_rules (fields)


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User(company=validated_data['company']
                    , username=validated_data['username']
                    , email=validated_data['email']
                    , first_name=validated_data['first_name']
                    , last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email', 'company', 'password',)
        # Init validator rule
        extra_kwargs = init_validator_rules (fields)


class ForgotPasswordValidationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        forgot_password = ForgotPasswordRequest(
            email=validated_data['email'])
        forgot_password.save()
        return forgot_password
    class Meta:
        model = ForgotPasswordRequest
        fields = ('email',)
class ForgotPasswordSerializer(serializers.ModelSerializer):
    reenter_password = serializers.CharField()
    class Meta:
        model = User
        fields = ('password','reenter_password')

class LoginSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'), username=username, password=password)

        if user:
            if not user.is_active:
                msg = 'User Account is Disabled'
                raise ValidationError(msg)
        else:
            msg = 'Unable to login with required credentials'
            raise ValidationError(msg)

        return user

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = init_validator_rules(fields)


class UserLoginSerializer(serializers.ModelSerializer):
    company = CompanySerializer(required=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('url', 'role','id', 'username', 'first_name', 'last_name', 'email', 'company', 'password','is_password_reset','is_tfa_enabled','enforce_tfa_enabled','is_tfa_setup_completed','tour_guide_enabled')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'email', 'title', 'phone','external_id','company')
        extra_kwargs = init_validator_rules(fields)

class EspressoContactSerializer(serializers.ModelSerializer):
    contact = ContactSerializer

    class Meta:
        model = EspressoContact
        fields = ( 'company','contact' )
        extra_kwargs = init_validator_rules(fields)
