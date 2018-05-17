from portalbackend.settings import RUN_UNIT_TEST
from tests.accounting.testcases.tc_balance_sheet import _001_BalanceSheetTestCase
from tests.accounting.testcases.tc_coa import _001_ChartofAccountsTestCase
from tests.accounting.testcases.tc_coa_map import _001_CoAMapTestCase
from tests.accounting.testcases.tc_connect import _001_ConnectionTestCase
from tests.accounting.testcases.tc_generate_statement import _001_GenerateStatementTestCase
from tests.accounting.testcases.tc_income_statement import _001_IncomeStatementTestCase
from tests.accounting.testcases.tc_trial_balance import _001_TrailBalanceTestCase

if RUN_UNIT_TEST:

    # @unittest - Tests Connection api calls
    tc_connect_view = _001_ConnectionTestCase

    # @unittest - Tests Chart of accounts api calls
    tc_chart_of_accounts_view = _001_ChartofAccountsTestCase

    # @unittest - Tests Chart of accounts maps api calls
    tc_coa_map_view = _001_CoAMapTestCase

    # @unittest - Tests Trail balance api calls
    tc_trial_balance_view = _001_TrailBalanceTestCase

    # @unittest - Tests Generate statements api calls
    tc_generate_statement_view = _001_GenerateStatementTestCase

    # @unittest - Tests Income statement api calls
    tc_income_statement_view = _001_IncomeStatementTestCase

    # @unittest - Tests Balance sheet api calls
    tc_balance_sheet_view = _001_BalanceSheetTestCase
