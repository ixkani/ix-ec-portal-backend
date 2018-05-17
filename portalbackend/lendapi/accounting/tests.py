from portalbackend.settings import RUN_UNIT_TEST

if RUN_UNIT_TEST:
    from tests.accounting.testcases import tc_connect, tc_coa, tc_coa_map, tc_trial_balance, tc_generate_statement, \
        tc_income_statement, tc_balance_sheet

    # @unittest - Tests Connection api calls
    tc_connect_view = tc_connect._001_ConnectionTestCase

    # @unittest - Tests Chart of accounts api calls
    tc_chart_of_accounts_view = tc_coa._001_ChartofAccountsTestCase

    # @unittest - Tests Chart of accounts maps api calls
    tc_coa_map_view = tc_coa_map._001_CoAMapTestCase

    # @unittest - Tests Trail balance api calls
    tc_trial_balance_view = tc_trial_balance._001_TrailBalanceTestCase

    # @unittest - Tests Generate statements api calls
    tc_generate_statement_view = tc_generate_statement._001_GenerateStatementTestCase

    # @unittest - Tests Income statement api calls
    tc_income_statement_view = tc_income_statement._001_IncomeStatementTestCase

    # @unittest - Tests Balance sheet api calls
    tc_balance_sheet_view = tc_balance_sheet._001_BalanceSheetTestCase
