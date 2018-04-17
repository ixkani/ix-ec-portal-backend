from rest_framework import status

from portalbackend.lendapi.accounts.models import Company
from portalbackend.lendapi.v1.accounting.third_party.quickbooks import QuickBooks
from portalbackend.lendapi.v1.accounting.third_party.xeros import XeroAccountings
from portalbackend.lendapi.v1.accounting.third_party.sage import SageAccountings
from portalbackend.lendapi.v1.accounting.utils import Utils


class Accounting:
    def get_instance_by_id(self, company_id):
        """
        This Wrapper method returns the object of the class for using in accounting system
        :param accounting_type:Name of the accounting system
        :return: Object of the accounting system to be accessed
        """
        accounting_type = Utils.capitalize(Utils.get_accounting_type(company_id))
        if accounting_type == Company.QUICKBOOKS:
            return QuickBooks()
        elif accounting_type == Company.XERO:
            return XeroAccountings()
        elif accounting_type == Company.SAGE:
            return SageAccountings()


