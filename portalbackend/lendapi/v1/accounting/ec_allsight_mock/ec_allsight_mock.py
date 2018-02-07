from .save_service import MappedAccountList
import json
import time


# This class parses the financial data and returns the data of Balancesheet and Income Statement

class AllSightMock:

    def __init__(self):
        pass

    @classmethod
    def initiate_allsight(cls, input_data):
        """
        :param input_data:Json [Model][Financials]
        :return: json of [Model][Financials] with Balancesheet and Income Statement
        """
        flag_verbose_output = False
        # from chart of accounts figure out the class: Asset, Liability, Equity, Income


        coa_base_list = {}
        for coa_account in input_data['Model']['Financials']['CustomerAccount']:
            account_category = coa_account['AccountCategory']
            base_account_id = coa_account['AccountId']
            if account_category in ['NONCURRENT','BANK','CURRENT','FIXED','INVENTORY','Fixed Asset', 'Bank', 'Other Current Asset', 'Accounts Receivable']:
                coa_base_list[base_account_id] = 'Asset'
            elif account_category in ['DIRECTCOSTS','SALES','CURRLIAB','LIABILITY','Other Current Liability', 'Long Term Liability', 'Credit Card',
                                      'Accounts Payable']:
                coa_base_list[base_account_id] = 'Liability'
            elif account_category in ['Equity','EQUITY']:
                coa_base_list[base_account_id] = 'Equity'
            else:
                coa_base_list[base_account_id] = 'Income'

        print("COA_BASE_LIST")
        print(coa_base_list)
        print("END_OF_COA_BASE_LIST")
        # sanity check - are all the trial balances 'in balance'?
        # that is, the sum of debits and credits should be equal
        print("\nChecking trial balances on the input file for errors")
        flag_input_tb_errors = False
        input_tb_summary = {}
        for tb in input_data['Model']['Financials']['CustomerTrialBalance']:
            total_debits = 0.0
            total_credits = 0.0
            total_assets = 0.0
            total_liabilities = 0.0
            total_equity = 0.0
            net_income_ytd = 0.0
            period = tb['Period']
            for tb_entry in tb['CustomerTrialBalanceItem']:
                debit = float(tb_entry['DebitAmount'])
                credit = float(tb_entry['CreditAmount'])
                total_debits += debit
                total_credits += credit
                account = tb_entry['AccountId']
                account_type = coa_base_list[account]
                if account_type == 'Asset':
                    total_assets += debit - credit
                elif account_type == 'Liability':
                    total_liabilities += credit - debit
                elif account_type == 'Equity':
                    total_equity += credit - debit
                else:  # net income
                    net_income_ytd += credit - debit
            total_equity += net_income_ytd
            input_tb_summary[period] = {
                # this will be used to compare with the output sample values
                'Assets': total_assets,
                'Liabilities': total_liabilities,
                'Equity': total_equity,
                'Net Income (YTD)': net_income_ytd
            }

            # print("Here i come")
            if flag_verbose_output:
                print('\tPeriod: {}\tAssets {:0.2f}, Liabilities {:0.2f}, Equity {:0.2f}, YTD NI {:0.2f}'.format(
                    period, total_assets, total_liabilities, total_equity, net_income_ytd))
            if abs(total_debits - total_credits) > 0.01:
                print('\t\tERROR: {}: Debits {:0.2f}, Credits {:0.2f}, Diff {:0.3f}'.format(
                    period, total_debits, total_credits, total_debits - total_credits))
                flag_input_tb_errors = True
            if abs(total_assets - (total_liabilities + total_equity)) > 0.01:
                print('\t\tERROR: Balance sheet not balanced: {:0.03f}'.format(
                    total_assets - (total_liabilities + total_equity)))
                flag_input_tb_errors = True
        print(flag_input_tb_errors)
        if flag_input_tb_errors:
            print('\tErrors found in input files -- correct and rerun')
        else:
            print('\tNo errors found')

        # create output
        print("\nProcessing the request")
        try:
            start_time = time.clock()
            ##################################################################################
            #
            # Start of Code block to process input
            #
            ##################################################################################

            # Step 1: Create Mapped Account List
            mapaccounts = MappedAccountList()

            # TODO: This is hardcoded for now - do this using the FinancialAccountTags in django
            # Step 2: add the accounts - Note the is_ytd_account=True value for the YTD Income account (ID: 3997 below)
            mapaccounts.add_map_account(map_account_id='4000', map_account_name='Non-Recurring Revenues',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='4500', map_account_name='Recurring Revenues',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='4900', map_account_name='Total Revenues',
                                        abstract=True, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='5000', map_account_name='Cost of Goods Sold',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='5999', map_account_name='Gross Profit',
                                        abstract=True, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='6100', map_account_name='Sales & Marketing Expenses',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='6200',
                                        map_account_name='Research & Development (excluding SRED)',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='6300', map_account_name='General & Administrative Expenses',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='6695', map_account_name='Total Operating Expenses',
                                        abstract=True, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='6699', map_account_name='EBITDA',
                                        abstract=True, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='6700', map_account_name='Interest Income (Expense)',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='6710', map_account_name='SR & ED',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='6720', map_account_name='IRAP/Grants Received',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='6730', map_account_name='Depreciation & Amortization',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='6740', map_account_name='Other Income (Expenses)',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='6900', map_account_name='Net Income',
                                        abstract=True, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='1000', map_account_name='Cash',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='1100', map_account_name='Accounts Receivables',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='1150', map_account_name='Tax Credit Receivable',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='1200', map_account_name='Other Current Assets',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='1499', map_account_name='Total Current Assets',
                                        abstract=True, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='1500', map_account_name='Fixed Assets',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='1600', map_account_name='Patents & Intangible Assets',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='1700', map_account_name='Other Assets',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='1999', map_account_name='Total Assets',
                                        abstract=True, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='2000',
                                        map_account_name='Accounts Payable and Accrued Liabilities',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='2050', map_account_name='Bank Debt',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='2100', map_account_name='Deferred Revenue',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='2150', map_account_name='Other Current Liabilities',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='2199', map_account_name='Total Current Liabilities',
                                        abstract=True, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='2500', map_account_name='Espresso Debt Outstanding',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='2600', map_account_name='Senior Secured Debt (to Espresso)',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='2700', map_account_name='Subordinated Debt (to Espresso)',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='2800', map_account_name='Shareholder Loans',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='2900', map_account_name='Other Liabilities',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='2999', map_account_name='Total Liabilities',
                                        abstract=True, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='3000', map_account_name='Share Capital and Contributed Capital',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='3100', map_account_name='Minority Equity Position',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='3200', map_account_name='Equity Portion of LT Debt',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='3900', map_account_name='Retained Earnings (Loss)',
                                        abstract=False, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='3997', map_account_name='Net Income Year to Date',
                                        abstract=True, is_ytd_account=True)  # NOTE THIS ENTRY!!!!!!!!!!!!!!!!!!!!
            mapaccounts.add_map_account(map_account_id='3998', map_account_name='Total Equity',
                                        abstract=True, is_ytd_account=False)
            mapaccounts.add_map_account(map_account_id='3999', map_account_name='Total L&E',
                                        abstract=True, is_ytd_account=False)

            # Step 3: process the input
            print("GOING_INSIDE_PROCESS_REQUEST")
            res = mapaccounts.process_request(input_data)

            ##################################################################################
            #
            # End of Code block to process input
            #
            ##################################################################################

            end_time = time.clock()
            print('\tTime elapsed: {:0.6f} seconds'.format(end_time - start_time))
        except Exception as ve:
            print('Error processing the input data: ' + str(ve))

        # Process output

        # print('\toutput.json - response json from process_request(input_data)')
        # with open('output.json', mode='wt') as f:
        #    f.write(json.dumps(res))

        return json.dumps(res)
