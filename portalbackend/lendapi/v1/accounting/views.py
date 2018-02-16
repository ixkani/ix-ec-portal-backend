import base64
import contextlib
import json
import os
import time

import requests
from django.shortcuts import redirect
from rest_framework import views
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from portalbackend.lendapi.accounting.csv_utils import CSVUtils
from portalbackend.lendapi.accounting.models import DefaultAccountTagMapping, CoAMap
from portalbackend.lendapi.accounting.models import TrialBalance, CoA
from portalbackend.lendapi.accounting.utils import AccountingUtils
from portalbackend.lendapi.accounts.models import Company
from portalbackend.lendapi.accounts.utils import AccountsUtils
from portalbackend.lendapi.reporting.models import FinancialStatementEntry
from portalbackend.lendapi.v1.accounting.ec_allsight_mock.ec_allsight_mock import AllSightMock
from portalbackend.lendapi.v1.accounting.serializers import CoASerializer, \
    TrialBalanceSerializer
from portalbackend.lendapi.v1.accounting.third_party import Accounting
from portalbackend.lendapi.v1.accounting.third_party.quickbooks import QuickBooks
# from portalbackend.lendapi.v1.accounting.utils import *
from portalbackend.lendapi.v1.accounting.utils import Utils
from .serializers import FinancialStatementEntrySerializer, CoAMapSerializer, UpdatedCoAMapSerializer


class Statement(views.APIView):
    """
    Generates the Financial Statements based on the users CoA, Map, and TrialBalance
    :return: Serialized Financial Statement Entries
    """

    # todo: we need to handle this response from All SIght more gracefully:
    # {'Meta': {'Status': 'FAILURE', 'DataModificationIndicator': 0,
    #          'Errors': [{'Message': 'Something went wrong.'}]}}
    def get(self, request, pk, *args, **kwargs):
        try:
            company = AccountsUtils.get_company(pk)

            # Build Request
            st = time.time()

            data = AccountingUtils.build_all_sight_save_request(company)

            # TODO: FISCAL YEAR CHANGE
            # Company's Current Fiscal Year End date
            print('setting fye dict')
            try:
                fye_dict = Utils.get_curr_prior_fiscal_year_end(company)
            except Exception:
                return Utils.dispatch_failure(request, 'FISCAL_YEAR_MISSING')
            print('splitting data into chuncks')
            slitted_data = Utils.spilt_input_to_chunk(data, fye_dict)

            error_tags = []
            # todo: this needs to be updated for production user and pass
            auth_header = 'Basic ' + base64.b64encode(bytes('user1:Password@1', 'utf-8')).decode()
            headers = {'Accept': 'application/json', 'content-type': 'application/json', 'Authorization': auth_header}

            proxy_dict_required = os.environ.get("PROXY_REQUIRED", 0)

            if os.environ.get('FIXIE_URL', ''):
                proxydict = {"http": os.environ.get('FIXIE_URL', ''), "https": os.environ.get('FIXIE_URL', '')}
            else:
                proxydict = {"http": 'http://fixie:40NHGHaz4KQBNC0@velodrome.usefixie.com:80',
                             "https": 'http://fixie:40NHGHaz4KQBNC0@velodrome.usefixie.com:80'}

            url_configured = True
            endpoint = os.environ.get('ALLSIGHT_URL', '')
            if endpoint == '' or endpoint is None:
                url_configured = False

            # TODO: FISCAL YEAR CHANGE
            try:
                # Send to All Sight
                balance_sheet_data = []
                income_statement_data = []

                for data in slitted_data:
                    print('^^^^^^^^^^^^^^^ processing tb data ')
                    # print(data)
                    print('^^^^^^^^^^^^^^^^^ tb data end')
                    st = time.time()
                    if url_configured:
                        if proxy_dict_required:
                            r = requests.post(endpoint, data=json.dumps(data), headers=headers, verify=True,
                                              proxies=proxydict)
                        else:
                            r = requests.post(endpoint, data=json.dumps(data), headers=headers, verify=True)

                        response = json.loads(r.text)
                    else:
                        json_response = AllSightMock.initiate_allsight(input_data=data)
                        response = json.loads(json_response)
                    print('{:.2f}s AS - SAVE Request'.format(time.time() - st))

                    # print('########## AS RESPONSE', response)
                    for entry in response["Model"]["Financials"]["BalanceSheet"]:
                        balance_sheet_data.append(entry)
                    for entry in response["Model"]["Financials"]["IncomeStatement"]:
                        income_statement_data.append(entry)
                    response["Model"]["Financials"]["BalanceSheet"] = balance_sheet_data
                    response["Model"]["Financials"]["IncomeStatement"] = income_statement_data

            except Exception:
                return Utils.dispatch_failure(request, 'ALL_SIGHT_CONNECTION')

            # Save to Database
            st = time.time()
            try:

                balance_sheet, bs_error_tags = AccountingUtils.parse_statement(request, company,
                                                                               response["Model"]["Financials"],
                                                                               FinancialStatementEntry.BALANCE_SHEET)

                income_statement, is_error_tags = AccountingUtils.parse_statement(request, company,
                                                                                  response["Model"]["Financials"],
                                                                                  FinancialStatementEntry.INCOME_STATEMENT)
                company = Company.objects.get(id=pk)

                if len(bs_error_tags) or len(is_error_tags):
                    if len(bs_error_tags):
                        error_tags += bs_error_tags
                    if len(is_error_tags):
                        error_tags += is_error_tags
                    if not company.is_tag_error_notified:
                        company.is_tag_error_notified = True
                        company.save()
                        Utils.send_error_tags(company=pk, user=request.user, error_tags=error_tags, response=response)
                else:
                    company.is_tag_error_notified = False
                    company.save()

                # combine them both and create them all at once
                income_statement.extend(balance_sheet)
                FinancialStatementEntry.objects.bulk_create(income_statement)

                credit_debit_equality = AccountingUtils.credit_debit_mismatch(company)
                if credit_debit_equality is not None:
                    if len(credit_debit_equality) > 0:
                        response['credit_debit_unequals'] = credit_debit_equality
                        print(response)
                # returns the response from All Sight
                return Utils.dispatch_success(request, response)
            except Exception as e:
                error = ["%s" % e]
                return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)

        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class CoaMapView(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        """
        Creates the CoAMap for a company from the CoA in the database
        """
        try:
            company = AccountsUtils.get_company(pk)
            coa = CoA.objects.filter(company=company)
            remap = request.GET.get('remap', None)
            if coa:
                default_mappings = DefaultAccountTagMapping.objects.filter(software=company.accounting_type.lower())

                if not default_mappings:
                    return Utils.dispatch_failure(request, "OBJECT_RESOURCE_NOT_FOUND")

                # todo: make sure abstract financial statement entry tags are not getting processed in the CoA Mapping
                try:
                    entries = AccountingUtils.create_coa_map(request, company, default_mappings, coa, remap)
                except Exception as e:
                    error = ["%s" % e]
                    return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)

                if len(entries) > 0:
                    serializer = CoAMapSerializer(entries, many=True)
                    return Utils.dispatch_success(request, serializer.data)
                return Utils.dispatch_success(request, "NO_DATA_CHANGES")
            return Utils.dispatch_failure(request, "OBJECT_RESOURCE_NOT_FOUND")

        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def post(self, request, pk, *args, **kwargs):
        try:
            company = AccountsUtils.get_company(pk)
            # print('CoAMap POST - request.data ', request.data)
            updated_maps = AccountingUtils.set_coa_map(company, request.data)
            serializer = UpdatedCoAMapSerializer(updated_maps, many=True)
            if len(serializer.data):
                return Utils.dispatch_success(request, serializer.data)
            return Utils.dispatch_success(request, "NO_DATA_CHANGES")

        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def put(self, request, pk, *args, **kwargs):
        """
        Updates verified by user in CoAMap for a company in the database
        """
        try:
            company = AccountsUtils.get_company(pk)
            coamap = CoAMap.objects.filter(company_id=company)
            for entry in coamap:
                entry.verified_by_user = False
                entry.save()
            return Utils.dispatch_success(request, 'COAMAP_UPDATED_SUCCESSFULLY')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def delete(self, request, pk, *args, **kwargs):
        try:
            if self.request.user.is_superuser:
                company = AccountsUtils.get_company(pk)
                if CoAMap.objects.filter(company=company).count():
                    CoAMap.objects.filter(company=company).delete()
                    return Utils.dispatch_success(request, 'DELETED_SUCCESSFULLY')
                else:
                    return Utils.dispatch_failure(request, "OBJECT_RESOURCE_NOT_FOUND")
            return Utils.dispatch_failure(request, 'UNAUTHORIZED_ACCESS')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class BalanceSheetView(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        """
        Gets the Balance Sheet Financial Statement Entries from the database
        Range can be specified by adding ?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD

        No date params will return all entries for the specified company.
        end_date param only will provide data for that specific period.
        A start_date without an end_date, it will cause an error.
        """
        try:
            company = AccountsUtils.get_company(pk)

            # todo: query variable is never used, and appears to be unncessary
            query, dates = Utils.validate_query(request, dateformat=True)

            # todo: figure out why order_by isn't workin on these query_sets, ordering added to model as workaround
            if not dates:
                print('########### not dates')
                queryset = FinancialStatementEntry.objects.filter(company=company,
                                                                  statement_type=FinancialStatementEntry.BALANCE_SHEET)
            else:
                if dates[0] == 'ERROR':
                    return Utils.dispatch_failure(request, dates[1])
                elif len(dates) == 2:
                    queryset = FinancialStatementEntry.objects.filter(company=company,
                                                                      statement_type=FinancialStatementEntry.BALANCE_SHEET,
                                                                      period_ending__range=(dates[0], dates[1]))
                elif len(dates) == 1:
                    print(dates)
                    queryset = FinancialStatementEntry.objects.filter(company=company,
                                                                      statement_type=FinancialStatementEntry.BALANCE_SHEET,
                                                                      period_ending=dates[0])
                else:
                    print(dates)
                    queryset = FinancialStatementEntry.objects.filter(company=company,
                                                                      statement_type=FinancialStatementEntry.BALANCE_SHEET)

            if queryset:
                serializer = FinancialStatementEntrySerializer(queryset, many=True)
                return Utils.dispatch_success(request, serializer.data)
            return Utils.dispatch_success(request, 'DATA_NOT_FOUND')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def post(self, request, pk, *args, **kwargs):
        """
        Parses the income statement and balance sheet sheet request, sent in the form of:
         {"BalanceSheet": [{
                "Period": "2016-01",
                "Account": "Value"},{..}]
            }
        """
        try:
            company = AccountsUtils.get_company(pk)
            try:
                entries, error_tags = AccountingUtils.parse_statement(request, company, request.data,
                                                                      FinancialStatementEntry.BALANCE_SHEET)
                FinancialStatementEntry.objects.bulk_create(entries)
            except Exception as e:
                error = ["%s" % e]
                return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)

            serializer = FinancialStatementEntrySerializer(entries, many=True)

            if len(serializer.data) > 0:
                return Utils.dispatch_success(request, serializer.data)
            return Utils.dispatch_success(request, 'NO_DATA_CHANGES')

        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def delete(self, request, pk, *args, **kwargs):
        try:
            if self.request.user.is_superuser:
                company = AccountsUtils.get_company(pk)
                if FinancialStatementEntry.objects.filter(statement_type=FinancialStatementEntry.BALANCE_SHEET,
                                                          company=company).count():
                    FinancialStatementEntry.objects.filter(statement_type=FinancialStatementEntry.BALANCE_SHEET,
                                                           company=company).delete()
                    return Utils.dispatch_success(request, 'DELETED_SUCCESSFULLY')
                return Utils.dispatch_success(request, "DATA_NOT_FOUND")
            return Utils.dispatch_failure(request, 'UNAUTHORIZED_ACCESS')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

            # return Response({"message": "Balance sheet objects have been deleted for {}".format(company.name)})


class IncomeStatementView(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        """
        Gets the Income Statement Financial Statement Entries from the database
        Range can be specified by adding ?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD


        No date params will return all entries for the specified company.
        end_date param only will provide data for that specific period.
        A start_date without an end_date, it will cause an error.
        """
        try:
            company = AccountsUtils.get_company(pk)

            query, dates = Utils.validate_query(request, dateformat=True)

            if not dates:
                queryset = FinancialStatementEntry.objects.filter(company=company,
                                                                  statement_type=FinancialStatementEntry.INCOME_STATEMENT)
            else:
                if dates[0] == 'ERROR':
                    return Utils.dispatch_failure(request, dates[1])
                elif len(dates) == 2:
                    queryset = FinancialStatementEntry.objects.filter(company=company,
                                                                      statement_type=FinancialStatementEntry.INCOME_STATEMENT,
                                                                      period_ending__range=(dates[0], dates[1]))
                elif len(dates) == 1:
                    queryset = FinancialStatementEntry.objects.filter(company=company,
                                                                      statement_type=FinancialStatementEntry.INCOME_STATEMENT,
                                                                      period_ending=dates[0])
                else:
                    queryset = FinancialStatementEntry.objects.filter(company=company,
                                                                      statement_type=FinancialStatementEntry.INCOME_STATEMENT)

            queryset = queryset.order_by('value')

            if queryset:
                serializer = FinancialStatementEntrySerializer(queryset, many=True)
                return Utils.dispatch_success(request, serializer.data)
            return Utils.dispatch_success(request, 'DATA_NOT_FOUND')

        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def post(self, request, pk, *args, **kwargs):
        """
        Parses the income statement and balance sheet sheet request, sent in the form of:
         {"IncomeStatement": [{
                "Period": "2016-01",
                "Account": "Value"},{..}]
            }
        """
        try:
            company = AccountsUtils.get_company(pk)

            try:
                entries, error_tags = AccountingUtils.parse_statement(request, company, request.data,
                                                                      FinancialStatementEntry.INCOME_STATEMENT)
                FinancialStatementEntry.objects.bulk_create(entries)
            except Exception as e:
                error = ["%s" % e]
                return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)

            serializer = FinancialStatementEntrySerializer(entries, many=True)
            if len(serializer.data) > 0:
                return Utils.dispatch_success(request, serializer.data)
            return Utils.dispatch_success(request, 'NO_DATA_CHANGES')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def delete(self, request, pk, *args, **kwargs):
        try:
            if self.request.user.is_superuser:
                company = AccountsUtils.get_company(pk)
                if FinancialStatementEntry.objects.filter(statement_type=FinancialStatementEntry.INCOME_STATEMENT,
                                                          company=company).count():
                    FinancialStatementEntry.objects.filter(statement_type=FinancialStatementEntry.INCOME_STATEMENT,
                                                           company=company).delete()
                    return Utils.dispatch_success(request, 'DELETED_SUCCESSFULLY')
                return Utils.dispatch_success(request, "DATA_NOT_FOUND")
            return Utils.dispatch_failure(request, 'UNAUTHORIZED_ACCESS')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

            # return Response({"message": "Income Statement objects have been deleted for {}".format(company.name)})


class CreateConnection(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            company_id = request.GET.get('company', None)
            # Check company is exists
            is_valid_company, message = Utils.check_company_exists(company_id)
            if not is_valid_company:
                return Utils.dispatch_failure(request, "RESOURCE_NOT_FOUND")
            return Accounting().get_instance_by_id(company_id).connect(request, company_id)
        except KeyError:
            print('not working')
            return redirect(request.META["HTTP_REFERRER"])
        except Exception as e:
            print(e)
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class QuickBooksAuthCodeHandler(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            company_id = request.GET.get('state', None)
            return Accounting().get_instance_by_id(company_id).auth_code_handler(request=request, pk=None)
        except Exception:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class XeroAuthCodeHandler(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk, *args, **kwargs):
        try:
            return Accounting().get_instance_by_id(pk).auth_code_handler(request, pk)
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class DisconnectToken(views.APIView):
    """
    Disconnects the Company from Accounting System
    """

    def get(self, request, pk, *args, **kwargs):
        try:
            return Accounting().get_instance_by_id(pk).disconnect(pk, request)
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class RefreshToken(views.APIView):
    """
    Refreshes the Token via an API call, instead of internal function
    """

    def get(self, request, pk, *args, **kwargs):
        try:
            return Accounting().get_instance_by_id(pk).refresh(pk, request)
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class TokenValid(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        """
        Check to see if the Accounting System token is still valid for the company
        """
        try:
            return Accounting().get_instance_by_id(pk).is_token_valid(pk, request)
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class ChartOfAccounts(views.APIView):
    parser_classes = (JSONParser, FileUploadParser)

    def get(self, request, pk, *args, **kwargs):
        """
        Gets the Chart of accounts from online and writes to database
        """
        # Check company is exists
        try:
            return Accounting().get_instance_by_id(pk).chart_of_accounts(pk, request)
        except Exception as e:
            print(e)
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def post(self, request, pk, *args, **kwargs):
        """
        Creates a chart of accounts from the request data, follows the format
        {"QueryResponse": { 'Account': [{
                                'Name': <string>,
                                'attr': <type>,
                                'CurrencyRef': {'value': 'USD', name: '..'},
                                'MetaData': {'CreatedTime': <timestamp>, 'LastUpdated:..}
                                },{..}
                            ]
                        }
                    }
        Sample response found at https://developer.intuit.com/docs/api/accounting/account
        """
        try:

            company = AccountsUtils.get_company(pk)
            if 'file' in request.data:
                file_type = CSVUtils.file_type(request.FILES['file'])
                if not file_type:
                    return Utils.dispatch_failure(request, "INVALID_FILE_FORMAT")
                request.FILES['file'].seek(0)

                if file_type == 'CSV':
                    # print('#--- processing coa csv')
                    csv_data = CSVUtils.format_request_csv(request.FILES['file'])
                    try:
                        coa_data = CSVUtils.process_chart_of_accounts_csv(company, csv_data)
                        if coa_data is "INVALID_CSV":
                            return Utils.dispatch_failure(request, 'INVALID_COA_CSV')
                        serializer = CoASerializer(coa_data, many=True)
                        if len(serializer.data) > 0:
                            return Utils.dispatch_success(request, serializer.data)
                        return Utils.dispatch_success(request, 'NO_DATA_CHANGES')

                    except Exception as e:
                        error = ["%s" % e]
                        return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)

                # elif file_type == 'Excel':
                #     excel_data = CSVUtils.format_request_excel(request.FILES)
                #     CSVUtils.silentremove('tmp.xlsx')
                #
                #     with contextlib.suppress(FileNotFoundError):
                #         os.remove('tmp.xlsx')

                return Utils.dispatch_failure(request, "OBJECT_RESOURCE_NOT_FOUND")

            else:
                try:
                    coas = QuickBooks.save_chart_of_accounts(company, request.data)
                except Exception as e:
                    error = ["%s" % e]
                    return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)
                try:
                    serializer = CoASerializer(coas, many=True)
                    if len(serializer.data) > 0:
                        return Utils.dispatch_success(request, serializer.data)
                    return Utils.dispatch_success(request, 'NO_DATA_CHANGES')
                except Exception as e:
                    return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

                    # return Response({"message": "todo implement csv parsing"})

        except Exception as e:
            print(e)
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def delete(self, request, pk, *args, **kwargs):
        try:
            if self.request.user.is_superuser:
                company = AccountsUtils.get_company(pk)
                if CoA.objects.filter(company=company).count():
                    CoA.objects.filter(company=company).delete()
                    return Utils.dispatch_success(request, 'DELETED_SUCCESSFULLY')
                else:
                    return Utils.dispatch_failure(request, "OBJECT_RESOURCE_NOT_FOUND")
            return Utils.dispatch_failure(request, 'UNAUTHORIZED_ACCESS')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')


class TrialBalanceView(views.APIView):
    parser_classes = (JSONParser, FileUploadParser)

    def get(self, request, pk, *args, **kwargs):
        """
        Gets the trial balance from online and writes to database
        """
        # Check company is exists
        try:
            return Accounting().get_instance_by_id(pk).trail_balance(pk, request)
        except Exception as e:

            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def post(self, request, pk, *args, **kwargs):
        """
        Creates Trial Balance from Posted json request, follows the format
        {"Header": {"Time": <timestamp>, "StartPeriod: "YYYY-MM-DD", "EndPeriod": "YYYY-MM-DD", "Currency"...},
         "Columns": { "Column": [ {"ColTitle": "Title", "ColType": "AccountType"}, {..}],
         "Rows": {"Row": [ {"ColData": [{"value": "Account", "id": <int>}, {..}], { "ColData"...}]
         }
        More info here: https://developer.intuit.com/docs/api/accounting/trial%20balance
        """
        try:
            company = AccountsUtils.get_company(pk)
            if 'file' in request.data:

                file_type = CSVUtils.file_type(request.FILES['file'])
                if not file_type:
                    return Utils.dispatch_failure(request, "INVALID_FILE_FORMAT")
                request.FILES['file'].seek(0)

                if file_type == 'CSV':
                    print('#--- processing tb csv')
                    try:
                        csv_data = CSVUtils.format_request_csv(request.FILES['file'])
                        tb_data = CSVUtils.process_trial_balance_csv(company, csv_data)
                        if not tb_data:
                            return Utils.dispatch_failure(request, 'INVALID_TB_DATE')
                        if tb_data is "INVALID_CSV":
                            return Utils.dispatch_failure(request, 'INVALID_TB_CSV')
                        serializer = TrialBalanceSerializer(tb_data, many=True)
                        if len(serializer.data) > 0:
                            return Utils.dispatch_success(request, serializer.data)
                        return Utils.dispatch_success(request, 'NO_DATA_CHANGES')
                    except Exception as e:
                        error = ["%s" % e]
                        return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)
                elif file_type == 'Excel':
                    try:
                        excel_data = CSVUtils.format_request_excel(request.FILES)

                        # wont be found on heroku
                        with contextlib.suppress(FileNotFoundError):
                            os.remove('tmp.xlsx')
                    except Exception as e:
                        error = ["%s" % e]
                        return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)

                        # return Response({"message": "Sent a CSV"})
            else:
                try:
                    entries = QuickBooks.save_trial_balance(company, request.data)
                    if entries is None:
                        return Utils.dispatch_failure(request, 'INVALID_TB_DATE')
                    TrialBalance.objects.bulk_create(entries)
                except Exception as e:
                    error = ["%s" % e]
                    return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)
                return Utils.dispatch_success(request, 'TRIAL_BALANCE_SAVE_SUCCESS')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

    def delete(self, request, pk, *args, **kwargs):
        try:
            if self.request.user.is_superuser:
                company = AccountsUtils.get_company(pk)
                if TrialBalance.objects.filter(company=company).count():
                    TrialBalance.objects.filter(company=company).delete()
                    return Utils.dispatch_success(request, 'DELETED_SUCCESSFULLY')
                else:
                    return Utils.dispatch_failure(request, "OBJECT_RESOURCE_NOT_FOUND")
            return Utils.dispatch_failure(request, 'UNAUTHORIZED_ACCESS')
        except Exception as e:
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')

            # return Response({"message": "Trial Balance objects have been deleted for {}".format(company.name)})


class LoginStatus(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            # Check company is exists
            is_valid_company, message = Utils.check_company_exists(pk)
            if not is_valid_company:
                return Utils.dispatch_failure(request, 'RESOURCE_NOT_FOUND')
            login_status = Utils.get_login_status(pk)
            if login_status:
                return Utils.dispatch_success(request, login_status.data)
            return Utils.dispatch_failure(request, 'UNAUTHORIZED_ACCESS')
        except Exception as e:
            print(e)
            return Utils.dispatch_failure(request, 'INTERNAL_SERVER_ERROR')
