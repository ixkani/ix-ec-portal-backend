import datetime

import pyotp
from django.shortcuts import reverse
from django.contrib.auth.models import User
from portalbackend.lendapi.accounts.models import User, Company, CompanyMeta, ScheduledMaintenance, Contact, \
    EspressoContact
from portalbackend.lendapi.v1.accounts.views import UserList, UserDetail, LoginView
from django.utils.timezone import utc

from tests.constants import TestConstants, CompanyConstant, UserConstant, ContactConstant


class TestUtils(object):

    @staticmethod
    def _admin_login(client):
        username = UserConstant.ADMIN_USERNAME
        password = UserConstant.ADMIN_PASSWORD
        client.login(username=username, password=password)

    @staticmethod
    def _user_login(client, username):
        client.logout()
        client.login(username=username, password=UserConstant.USER_PASSWORD)

    @staticmethod
    def _create_superuser():
        username = UserConstant.ADMIN_USERNAME
        password = UserConstant.ADMIN_PASSWORD
        email = UserConstant.ADMIN_EMAIL
        user = User.objects.create_superuser(username, email, password)
        user.save()
        return user

    @staticmethod
    def _create_user(username, company_id):
        company = Company.objects.filter(id=company_id).first()
        user = User.objects.create_user(username, UserConstant.USER_EMAIL, UserConstant.USER_PASSWORD)
        user.company = company
        user.save()
        return user

    @staticmethod
    def _post(client, string, data):
        response = client.post(string, data,format='json',HTTP_HOST='espresso-ix-backend.herokuapp.com')
        print(response)
        return response.status_code, response.data

    @staticmethod
    def _post_with_args(client, string, args, data):
        response = client.post(reverse(string, args=[args]), data ,format='json')
        return response.status_code, response.data

    @staticmethod
    def _get(client, string, ):
        response = client.get(reverse(string),format='json')
        return response.status_code, response.data

    @staticmethod
    def _get_with_args(client, string, args):
        if type(args) is list:
            response = client.get(reverse(string, args=args),format='json')
        else:
            response = client.get(reverse(string, args=[args]),format='json')
        return response.status_code, response.data

    @staticmethod
    def _put(client, string, data):
        response = client.put(reverse(string), data,format='json')
        return response.status_code, response.data

    @staticmethod
    def _put_with_args(client, string, args, data):
        if type(args) is list:
            response = client.put(reverse(string, args=args), data,format='json')
        else:
            response = client.put(reverse(string, args=[args]), data,format='json')
        return response.status_code, response.data

    @staticmethod
    def _delete(client, string, args):
        if type(args) is list:
            response = client.delete(reverse(string, args=args),format='json')
        else:
            response = client.delete(reverse(string, args=[args]),format='json')
        return response.status_code, response.data

    @staticmethod
    def _create_company(id, name):
        company = Company.objects.create(id=id, name=name, external_id=CompanyConstant.DEFAULT_COMPANY_EXTERNALID,
                                         website=CompanyConstant.DEFAULT_COMPANY_WEBSITE,
                                         employee_count=CompanyConstant.DEFAULT_COMPANY_EMPLOYEE_COUNT)
        company.save()
        return company

    @staticmethod
    def _create_companymeta(id):
        company_meta = CompanyMeta.objects.get(company_id=id)
        company_meta.monthly_reporting_current_period = CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD
        company_meta.monthly_reporting_next_period = CompanyConstant.COMPANY_NEXT_REPORT_PERIOD
        company_meta.save()

    @staticmethod
    def _create_contact(id):
        company = Company.objects.get(id=1)
        contact = Contact.objects.create(
            company=company,
            first_name=ContactConstant.DEFAULT_CONTACT_FIRST_NAME,
            external_id=ContactConstant.DEFAULT_CONTACT_EXTERNALID,
            last_name=ContactConstant.DEFAULT_CONTACT_LAST_NAME,
            email=ContactConstant.DEFAULT_CONTACT_EMAIL,
            title=ContactConstant.DEFAULT_CONTACT_TITLE
        )
        contact.save()

    @staticmethod
    def _create_espresso_contact(id, cid):
        company = Company.objects.get(id=id)
        contact = Contact.objects.get(id=cid)
        espresso_contact = EspressoContact.objects.create(company=company,contact=contact)
        espresso_contact.save()

    @staticmethod
    def _create_scheduled_maintenance():
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        scheduled_maintenance = ScheduledMaintenance.objects.create(
            message="Sever under Maintaince",
            start_time=now,
            end_time=now + datetime.timedelta(hours=1),
            is_active=True
        )
        scheduled_maintenance.save()

    @staticmethod
    def _delete_company_meta(company_id):
        meta = CompanyMeta.objects.get(company_id=company_id)
        meta.delete()

    @staticmethod
    def _update_scheduled_maintenance():
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        scheduled_maintenance = ScheduledMaintenance.objects.all()[0]
        scheduled_maintenance.is_active = False
        scheduled_maintenance.save()

    @staticmethod
    def _get_Totp(code):
        return pyotp.TOTP(code).now()
