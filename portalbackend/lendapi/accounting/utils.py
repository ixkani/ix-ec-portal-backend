import re
from django.http import Http404, HttpResponseServerError
from django.utils import timezone
from datetime import timedelta, date,datetime
import datetime
import time
from django.utils.timezone import utc

from rest_framework.response import Response

from portalbackend.lendapi import constants
from portalbackend.lendapi.accounting.models import AccountingOauth2, CoA,LoginInfo
from portalbackend.lendapi.accounting.models import FinancialStatementEntryTag, TrialBalance, CoAMap
from portalbackend.lendapi.reporting.models import FinancialStatementEntry
from django.db import transaction
import calendar

class AccountingUtils(object):
    """
    A collection of functions that are used within the Accounting views and functions
    """
    @staticmethod
    def updateAccountingSession(company, accessToken, refreshToken, realmId):
        """
        Updates the Accounting Session Saved inside the database
        :param company:
        :param accessToken:
        :param refreshToken:
        :param realmID:
        :return:
        """
        token = AccountingOauth2.objects.filter(company=company).first()
        if token:
            token.accessToken = accessToken
            token.refreshToken = refreshToken
            if token.realmId != realmId:
                token.realmId = realmId
        else:
            token = AccountingOauth2(company=company, accessToken=accessToken,
                                     refreshToken=refreshToken, realmId=realmId)
        token.save()
        return token

    @staticmethod
    def get_credentials(request):
        """
        Fetches the accounting authentication credentials by the request user (deprecated)
        :param request:
        :return:
        """
        if request.user.company:
            token = AccountingOauth2.objects.filter(company=request.user.company).first()
            if token:
                return token
            raise Http404
        else:
            raise Http404

    @staticmethod
    def get_status_object(company):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        time_threshold = now - datetime.timedelta(hours=2)
        try:
            return LoginInfo.objects.filter(company=company, created__range=(time_threshold, now)).first()
        except LoginInfo.DoesNotExist:
            raise Http404

    @staticmethod
    def get_credentials_by_company(company):
        """
        Fetches the accounting authentication credentials by company object
        :param company:
        :return:
        """
        token = AccountingOauth2.objects.filter(company=company).first()
        return token

    @staticmethod
    def create_mapping_dict(queryset):
        """
        Converts a queryset of the default map into a useable dictionary
        :param queryset:
        :return:
        """
        d = {}
        for mapping in queryset:
            d[mapping.account_category.lower()] = {"default_map_id": mapping.default_map_id,
                                                   "default_map_name": mapping.default_map_name}
        return d

    @staticmethod
    def parse_statement(request,company, data, statement_type):
        """
        Parses the income statement and balance sheet sheet request, sent in the form of:
         {"StatementType": [{"Period": "2016-01"},...]}, statement type can either be BalanceSheet or IncomeStatement
        :param company:
        :param data:
        :param statement_type: The type of sheet that is being parsed
        :return:
        """
        fixed_fields = ("Period", "CreatedTimestamp", "LastUpdatedTimestamp", "SourceName", "SourceKey")
        entries = []
        error_tags = []
        monthly_report = None
        tags = FinancialStatementEntryTag.objects.all()

        tag_lookup = {}
        sight_tag_lookup = {}
        for tag in tags:
            sight_tag_lookup[tag.all_sight_name] = tag.tag_id
            tag_lookup[str(tag.tag_id)] = {"id": tag.id, "short_label": tag.short_label}

        # All Sight sends back BalanceSheet not Balance Sheet, so we need to translate (same for income statement)
        for month in data[statement_type.replace(" ", "")]:
            y, m = map(int, month["Period"].split('-'))
            num_days = calendar.monthrange(y, m)[1]
            period = datetime.date(y, m, num_days)

            for key, value in month.items():
                if value is None:
                    value = '0.00'

                if key not in fixed_fields:
                    check_key_exists = sight_tag_lookup.get (key, None)
                    if check_key_exists is None:
                        tag_key = str (key)
                    else:
                        tag_key = sight_tag_lookup[key]

                    try:

                        cur_tag = tag_lookup[str(tag_key)]
                    except KeyError as e:
                        print('### WARNING ### - tag id ', tag_key, ' not found in financial statement entry tag map')
                        if tag_key not in error_tags:
                            error_tags.append(tag_key)

                    else:
                        rows_affected = FinancialStatementEntry.objects.filter(
                                            fse_tag_id=cur_tag['id'],
                                            period_ending=period,
                                            company=company,
                                            statement_type=statement_type).update(value=value)

                        # 0 rows affected == it doesn't exist
                        if rows_affected == 0:
                            # these will be bulk created
                            entry = FinancialStatementEntry(company=company, period_ending=period,
                                                            entry_name=cur_tag['short_label'],
                                                            value=value, currency='CAD',
                                                            fse_tag_id=cur_tag['id'],
                                                            statement_type=statement_type)
                            entries.append(entry)
        return entries,error_tags
    @staticmethod
    def credit_debit_mismatch(company):
        """
        Method compares the Total Assets and Total L&E and returns the period if both the value are not equal
        """
        try:
            total_liabilities_equity = FinancialStatementEntryTag.objects.get(
                tag_category="total_liabilities_equity")
            total_assets = FinancialStatementEntryTag.objects.get(tag_category="total_assets")
            financial_statement_entry_equity = FinancialStatementEntry.objects.filter(
                fse_tag_id=total_liabilities_equity,
                company=company,
                statement_type=FinancialStatementEntry.BALANCE_SHEET)
            dict_credits = {}
            dict_debits = {}
            for financial_statement_entry_object in financial_statement_entry_equity:
                dict_credits[str(financial_statement_entry_object.period_ending)] = int(
                    financial_statement_entry_object.value)
            financial_statement_entry_assets = FinancialStatementEntry.objects.filter(
                fse_tag_id=total_assets,
                company=company,
                statement_type=FinancialStatementEntry.BALANCE_SHEET)
            for financial_statement_entry_object in financial_statement_entry_assets:
                dict_debits[str(financial_statement_entry_object.period_ending)] = int(
                    financial_statement_entry_object.value)
            credit_debit_mismatch = []
            for key in dict_credits:
                if key in dict_debits:
                    val1 = dict_credits[key]
                    val2 = dict_debits[key]
                    if val1 != val2:
                        credit_debit_mismatch.append(key)
            print(credit_debit_mismatch)
            return credit_debit_mismatch
        except Exception as e:
            print(str(e))
            return None

    @staticmethod
    def get_stripped_tags():
        """
        Retrieves stripped down version of Financial Statement Entry tags
        :return:
        """
        d = {}
        # some tags are formatted differently in the post than in the structure
        special_cases = {'TotalLE': 'TotalLiabilityAndEquity',
                         'EquityPortionofLTDebt': 'EquityPositionOfLTDebt',
                         'ShareCapitalandContributedCapital': 'ShareAndContributedCapital',
                         'NetIncome': 'NetIncomeYTD',
                         'SREDITCReceivable': 'SREDReceivable',
                         'PatentsIntangibleAssets': 'PatentsAndIntangibleAssets',
                         'TotalRevenues': 'TotalRevenue',
                         'DepreciationAmortization': 'DepreciationAndAmortization',
                         'SRED': 'SREDAccrual',
                         'RDGrossexcludingSRED': 'RDGrossMinusExcludingSRED',
                         'AccountsReceivables': 'AccountReceivables'
                         }
        tags = FinancialStatementEntryTag.objects.all()
        for tag in tags:
            stripped = tag.short_label
            stripped = stripped.replace(' ', '')
            repl = re.sub('[^a-zA-Z0-9 \n\.]', '', stripped)
            if repl in special_cases:
                repl = special_cases[repl]
            d[repl] = tag
        ld = {k.lower(): v for k, v in d.items()}
        return ld

    @staticmethod
    def build_all_sight_save_request(company):
        data = {"SourceName": "CustomerProfile",
                "SourceKey": company.id,
                "Model": {
                    "Financials": {}
                    }
                }
        trial_balances = TrialBalance.objects.filter(company=company)
        grouped = dict()
        for obj in trial_balances:
            grouped.setdefault(obj.period.strftime("%Y-%m"), []).append(obj)
        data["Model"]["Financials"]["CustomerTrialBalance"] = []
        for key, month_data in grouped.items():
            subdata = {"Period": key, "RecordedTimestamp": timezone.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
                       "Version": "1", "CustomerTrialBalanceItem": []}
            for entry in month_data:
                subdata["CustomerTrialBalanceItem"].append({
                    "AccountId": str(entry.gl_account_id),
                    "AccountName": entry.gl_account_name,
                    "CreditAmount": str(entry.credit),
                    "DebitAmount": str(entry.debit)
                })
            data["Model"]["Financials"]["CustomerTrialBalance"].append(subdata)

        data["Model"]["Financials"]["CustomerAccount"] = []
        coas = CoA.objects.filter(company=company)
        for coa in coas:
            subdata = {
                "AccountId": str(coa.gl_account_id),
                "AccountName": coa.gl_account_name,
                "AccountCategory": coa.gl_account_type
            }
            data["Model"]["Financials"]["CustomerAccount"].append(subdata)

        data["Model"]["Financials"]["CustomerAccountMapping"] = []
        coamaps = CoAMap.objects.filter(company=company)
        for mapping in coamaps:
            subdata = {
                "FromAccountId": str(mapping.cust_account_id),
                "FromAccountName": mapping.cust_account_name,
                "ToAccountId": str(mapping.espresso_account_id),
                "ToAccountName": mapping.espresso_account_name,
            }
            data["Model"]["Financials"]["CustomerAccountMapping"].append(subdata)
        return data

    @staticmethod
    def create_coa_map(request,company, default_mappings, coa, remap):
        mappings = AccountingUtils.create_mapping_dict(default_mappings)
        saved_mappings = []

        for account in coa:
            try:
                # since we're forced to match on strings, we strip out all non-numeric / non-alpha characters
                # and lower all alpha to reduce the chance for mis match between submitted and default tag names
                lookup_key = re.sub('[^a-zA-Z0-9]', '', account.gl_account_type).lower()
                default_map_dict = mappings[lookup_key]
            except KeyError:
                # error = ["%s" % e]
                # return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)
                # todo: log this to a file, and send a warning to the system admin to check
                print({"error": "no mapping for account type: {} ".format(account.gl_account_type)})
            else:
                entry = CoAMap.objects.filter(company=company, cust_account_id=account.gl_account_id).first()
                # send back anything that's new, so it can be mapped
                if not entry:
                    mapping = CoAMap(company=company,
                                     cust_account_name=account.gl_account_name,
                                     cust_account_id=account.gl_account_id,
                                     espresso_account_id=default_map_dict["default_map_id"],
                                     espresso_account_name=default_map_dict["default_map_name"])
                    mapping.save()
                    saved_mappings.append(mapping)
                else:
                    # and also send back anything that hasn't been verified by the user
                    # verification doesn't occur until the monthly report is signed off, because the
                    # remapping exercise done by the UI may need to take place several times before it can be considered
                    # valid
                    if not entry.verified_by_user:
                        saved_mappings.append(entry)

        return saved_mappings

    @staticmethod
    def set_coa_map(company, coamap):
        updated_mappings = []
        for account in coamap:
            coamapping = CoAMap.objects.filter(company=company, cust_account_id=account["cust_account_id"]).first()

            tag = FinancialStatementEntryTag.objects.filter(description=account["espresso_account_name"],
                                                            tag_id=account["espresso_account_id"]).first()

            if not tag:
                tag = FinancialStatementEntryTag.objects.filter(tag_id=account["espresso_account_id"]).first()
            coamapping.espresso_account_id = tag.tag_id
            coamapping.espresso_account_name = tag.description
            coamapping.is_mapped = True
            coamapping.save()

            updated_mappings.append(coamapping)

        return updated_mappings

    @staticmethod
    def get_gl_account_id_by_name(company, account_name):
        gl_id = ''

        coa = CoA.objects.filter(company=company, gl_account_name=account_name).first()
        if coa:
            gl_id = coa.gl_account_id

        return gl_id
