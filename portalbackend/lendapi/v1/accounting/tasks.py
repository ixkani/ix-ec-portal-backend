from portalbackend.lendapi.accounting.models import TrialBalance
from portalbackend.celery import app
from portalbackend.lendapi.accounting.utils import AccountingUtils
from portalbackend.lendapi.accounts.models import CompanyMeta,Company
from portalbackend.lendapi.accounts.utils import AccountsUtils
from portalbackend.lendapi.v1.accounting.utils import Utils
from xero.auth import PublicCredentials,PrivateCredentials
from portalbackend.lendapi.accounting.models import AccountingOauth2
from . import settings
from .third_party.xeros import XeroAccountings
import datetime
import time
from dateutil.relativedelta import relativedelta
from xero import Xero

@app.task
def trial_balance_for_period(pk, period_offset):
    cm = CompanyMeta.objects.filter(company_id=pk).first()
    cm.save()

    company = AccountsUtils.get_company(pk)
    st = time.time()
    credentials = AccountingUtils.get_credentials_by_company(company)

    if not credentials:
        return

    if not cm.monthly_reporting_current_period:
        return

    if company.accounting_type == Company.QUICKBOOKS:
        period = cm.monthly_reporting_current_period - relativedelta(months=+period_offset, day=31)
        # print('##### Getting TRIAL BALANCE for period ', period)

        query = '?start_date=' + period.strftime('%Y-%m-1') + '&end_date=' + period.strftime('%Y-%m-%d')
        # print('####### QBO TB QUERY ', query)

        # for query in query_list:
        trial_balance_response, status_code = Utils.get_trial_balance(credentials.accessToken, credentials.realmId, query)

        if status_code >= 400:
            bearer = Utils.get_bearer_token_from_refresh_token(credentials.refreshToken)
            new_credentials = AccountingUtils.updateAccountingSession(company, bearer.accessToken,
                                                                      bearer.refreshToken, credentials.realmId)
            trial_balance_response, status_code = Utils.get_trial_balance(new_credentials.accessToken,
                                                                          new_credentials.realmId, query)
            if status_code >= 400:
                return

        from .third_party.quickbooks import QuickBooks
        entries = QuickBooks.save_trial_balance(company, trial_balance_response)
        TrialBalance.objects.bulk_create(entries)

    if company.accounting_type == Company.XERO:
        period = cm.monthly_reporting_current_period - relativedelta(months=+period_offset, day=31)
        # params = {'fromDate': str(period.strftime('%Y-%m-01')), 'toDate': str(period.strftime('%Y-%m-%d'))}
        params = {'date': str(period.strftime('%Y-%m-%d'))}
        auth = Utils.get_xero_auth(pk)

        if settings.XERO_ACCOUNT_TYPE == "PRIVATE":
            credentials = PrivateCredentials(**auth)
        else:
            credentials = PublicCredentials(**auth)
        xero = Xero(credentials)
        trialbalance = xero.reports.get('TrialBalance',
                                        params=params)
        XeroAccountings.save_trial_balance(company, trialbalance[0])

    # print('{:.2f}s Elapsed'.format(time.time() - st))

    # print('Took {:.2f}s Total'.format(time.time() - st))

    cm.trialbalance_last_refresh_date = datetime.datetime.now()
    cm.trialbalance_dl_complete = True
    cm.save()

    return
