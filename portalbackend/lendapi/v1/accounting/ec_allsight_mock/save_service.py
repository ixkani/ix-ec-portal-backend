import copy

class MappedAccountList:
    """
    A class to manage account mappings. Collapses a trial balance from

    Nomenclature:
    map_account = Espresso's financial tags. The thing we are mapping to.
    base_account = Clients financial accounts. The thing we are mapping from.

    many base_accounts will map to a single map_account. it is an error to map the same
    base_account to a single map_account.

    Usage:
    1. create the class instance
    2. add the map accounts with 'add_map_account'
    3. create the mappings - for each base account, call  'add_mapping'
    4. for each period (to process a particular trial balance):
        4a. Add a period name with 'add_period' in order from earliest to latest. The first entry is assumed to
            be the first period in the fiscal year. ORDERING IS IMPORTANT.
        4b. for each base account in a trial balance for that period, call 'add_value'
    5. process the data by calling 'process_values'
    6. use get_map_account_name, get_map_account_value to extract information, or alternatively
       get an array of tuples (map_id, map_name, value) for a given period using 'get_period_normalized_values'

    NOTE: Values are + for debit, - for credit
    """

    BALANCE_SHEET_ACCOUNT = 1
    INCOME_STATEMENT_ACCOUNT = 2

    def __init__(self):
        self.__map_account_list = {}  # a dictionary of account values
        self.__period_values = {}  # a dictionary (indexed by period) of
        #    dictionaries (indexed by map_accounts) of values
        self.__period_names = []  # an ordered array of period names, earliest to latest
        self.YEAR_TO_DATE_INCOME_ACCOUNT_ID = None

    def debug(self):
        print(self.__map_account_list)
        print(type(self.__map_account_list))
        print(type(self.__map_account_list.keys()))
        for x in self.__map_account_list:
            print(str(x) + "\t" + str(type(x)))
        print([x['id'] for x in self.__map_account_list.values()])

    def add_map_account(self, map_account_id: str, map_account_name: str, abstract=False, is_ytd_account=False):
        """
        Adds a map account
        :param map_account_id: ID used to identify the map account
        :param map_account_name: displayed text string
        :param abstract: is this account abstract (boolean value)
        :param is_ytd_account: is this a YTD account? (boolean value)
        :return:
        """
        # check that the account has not yet been added
        if map_account_id not in self.__map_account_list.keys():
            # add account to __map_account_list
            self.__map_account_list[map_account_id] = {
                'id': map_account_id,  # id of the map account
                'type': self.BALANCE_SHEET_ACCOUNT if int(map_account_id) <= 3999 else self.INCOME_STATEMENT_ACCOUNT,
                'name': map_account_name,  # name of the map account
                'mapping': [],  # base account id's that map to this account
                'abstract': abstract
            }
            if is_ytd_account:
                self.YEAR_TO_DATE_INCOME_ACCOUNT_ID = map_account_id

    def add_mapping(self, map_account_id: str, base_account_id: str):
        if map_account_id not in self.__map_account_list.keys():
            raise ValueError('Account ID {} does not exist'.format(map_account_id))
        if map_account_id == self.YEAR_TO_DATE_INCOME_ACCOUNT_ID:
            raise ValueError('Cannot map to YTD income account')
        self.__map_account_list[map_account_id]['mapping'] += [base_account_id]

    def add_period(self, period: str):
        self.__period_names += [period]
        self.__period_values[period] = {str(x): 0.0 for x in self.get_map_account_ids()}
        pass

    def __find_map_account(self, base_account_id: str):
        for map_acc in self.__map_account_list.values():
            if base_account_id in map_acc['mapping']:
                return map_acc['id']
        raise ValueError("Cannot find '" + base_account_id + "'")

    def add_value(self, base_account_id: str, period: str, value: float):
        map_account_id = self.__find_map_account(base_account_id)
        if period not in self.__period_names:
            raise ValueError("Invalid period '" + period + "'")
        self.__period_values[period][map_account_id] += value

    def process_values(self, presort_names=False):
        # make sure there is something to process
        if len(self.__period_names) < 2:
            return  # nothing to do if there are 0 or 1 periods.

        # make a list of map accounts needed to be processed
        map_accounts_to_process = [x['id'] for x in self.__map_account_list.values() if
                                   x['type'] == self.INCOME_STATEMENT_ACCOUNT]

        # updates the YTD values to per period values
        prev_period = None
        prev_tb_map = None
        period_names_list = copy.deepcopy(self.__period_names)
        if presort_names:
            period_names_list.sort()
            print(period_names_list)
        else:
            print("Test of sort list")
            tmp = period_names_list.copy()
            print("Before: " , tmp)
            tmp.sort()
            print("After: ", tmp)
            print(period_names_list)
            print('^^^^^^^^^^^^^^^^^^^^^^^')

        for period in period_names_list:
            tb_map = self.__period_values[period]
            print(f"Processing period {period} - prev period: {prev_period}")

            # step A: make sure the amounts are complete (i.e. sum(map_account_values) = 0)
            # this is purely a sanity check to make sure the initial values are correct.
            total = 0
            for val in tb_map.values():
                total += val
            if abs(total) >= 0.01:
                raise Exception("Trial balance not balanced: net = {:0.3f}".format(total))

            # step B: diff all non-balance sheet accounts -- skip the first period
            prev_tb_map_storage = copy.deepcopy(tb_map)  # make a copy of the old tb before we modify it
            ytd_value = 0.0  # store the ytd values for income statement accounts
            for account_id in tb_map.keys():
                tb_map[account_id] = round(tb_map[account_id], 2)
                if account_id in map_accounts_to_process:
                    ytd_value += tb_map[account_id]
                    if prev_period is not None:
                        tb_map[account_id] -= prev_tb_map[account_id]
            tb_map[self.YEAR_TO_DATE_INCOME_ACCOUNT_ID] = ytd_value  # update YTD account
            print(f"\tNRev value period {period}: value = {tb_map['4000']}")

            # step C: flip the signs of the various accounts if normally credit balances
            total_assets = 0.0
            total_liabilities = 0.0
            total_equity = 0.0
            net_income = 0.0
            for account_id in tb_map.keys():
                account = int(account_id)
                if account in range(1000, 2000):
                    # Assets
                    total_assets += tb_map[account_id]
                elif account in range(2000, 3000):
                    # Liabilities
                    tb_map[account_id] *= -1
                    total_liabilities += tb_map[account_id]
                elif account in range(3000, 4000):
                    # Equities
                    tb_map[account_id] *= -1
                    total_equity += tb_map[account_id]
                elif account in range(4000, 5000):
                    # Revenues
                    tb_map[account_id] *= -1
                    net_income += tb_map[account_id]
                else:
                    # Expenses
                    net_income -= tb_map[account_id]
            # print("\t{}\tAssets: {:0.2f}\tLiabilites: {:0.2f}\tEquity: {:0.2f}\tNet Income: {:0.2f}".format(
            #     period,
            #     total_assets,
            #     total_liabilities,
            #     total_equity,
            #     net_income))

            # step D: process the abstract accounts
            tb_map['4900'] = tb_map['4000'] + tb_map['4500']  # Total Revenue (credit value)
            tb_map['5999'] = tb_map['4900'] - tb_map['5000']  # Gross Profit
            tb_map['6695'] = tb_map['6100'] + tb_map['6200'] + \
                             tb_map['6300']  # Total operating expenses
            tb_map['6699'] = tb_map['5999'] - tb_map['6695']  # EBITDA
            tb_map['6900'] = tb_map['6699'] - tb_map['6710'] - \
                             tb_map['6720'] - tb_map['6730'] - \
                             tb_map['6740']  # net income
            tb_map['1499'] = tb_map['1000'] + tb_map['1100'] + \
                             tb_map['1150'] + tb_map['1200']  # Total current assets
            tb_map['1999'] = tb_map['1499'] + tb_map['1500'] + \
                             tb_map['1600'] + tb_map['1700']  # Total assets
            tb_map['2199'] = tb_map['2000'] + tb_map['2050'] + \
                             tb_map['2100'] + tb_map['2150']  # Total current liabilities
            tb_map['2999'] = tb_map['2199'] + tb_map['2500'] + \
                             tb_map['2600'] + tb_map['2700'] + \
                             tb_map['2800'] + tb_map['2900']  # Total liabilities
            tb_map['3998'] = tb_map['3000'] + tb_map['3100'] + \
                             tb_map['3200'] + tb_map['3900'] + \
                             tb_map['3997']  # Total Equity
            tb_map['3999'] = tb_map['3998'] + tb_map['2999']  # Total liabilities & equity

            # check that it balances etc.
            balance = tb_map['1999'] - tb_map['3999']
            if abs(balance) >= 0.01:
                print("Out of balance: ${:0.2f}".format(balance))
            if abs(total_assets - tb_map['1999']) >= 0.01:
                raise AssertionError(
                    "Total assets not matching map account: diff = ${:0.2f}".format(
                        abs(total_assets - tb_map['1999'])))
            if abs(total_liabilities - tb_map['2999']) >= 0.01:
                raise AssertionError(
                    "Total liabilities not matching map account: diff = ${:0.2f}".format(
                        abs(total_liabilities - tb_map['2999'])))
            if abs(total_equity - tb_map['3998']) >= 0.01:
                raise AssertionError(
                    "Total equity not matching map account: diff = ${:0.2f}".format(
                        abs(total_equity - tb_map['3998'])))
            if abs(net_income - tb_map['6900']) >= 0.01:
                raise AssertionError(
                    "Net Income not matching map account: diff = ${:0.2f}".format(
                        abs(net_income - tb_map['6900'])))

            # End of loop: process the next period
            prev_period = period
            prev_tb_map = prev_tb_map_storage

        return  # End of process_values function

    def get_map_account_name(self, account_id: str):
        return self.__map_account_list[account_id]['name']

    def get_map_account_value(self, account_id: str, period: str):
        return self.__period_values[period][account_id]

    def get_map_account_ids(self):
        return [x['id'] for x in self.__map_account_list.values()]

    def get_period_normalized_values(self, period: str):
        return [(
            map_acc['id'],
            map_acc['name'],
            map_acc['type'],
            self.get_map_account_value(account_id=map_acc['id'], period=period)
        ) for map_acc in self.__map_account_list.values()]

    def get_periods(self):
        return self.__period_names

    def process_request(self, input_data, presort_names=False):
        """
        Maps trial balance data to output

        Assumption:
            1. the data is arranged so the earliest customer trial balance is always the start of a new year.
                -- if False, mapped values will be wrong, but it will NOT throw an error
            2. The COA map is complete (i.e. no missing accounts)
                -- if False, it will return an error with a very terse and rude error message

        :param input_data: A dictionary request to be processed - cf. documentation on request from Allsight
        :param presort_names: Should period names be sorted prior to processing?
        :return:
        """
        # Step 1: make sure the mapped accounts have been set up
        coa_map = input_data['Model']['Financials']['CustomerAccountMapping']
        for map_entry in coa_map:
            if map_entry['ToAccountId'] not in self.__map_account_list.keys():
                raise ValueError('Map account {} not set up - COA map invalid'.format(map_entry['ToAccountId']))

        # Step 2: add the mappings
        coa_map = input_data['Model']['Financials']['CustomerAccountMapping']
        for map_entry in coa_map:
            self.add_mapping(map_account_id=map_entry['ToAccountId'],
                             base_account_id=map_entry['FromAccountId'])

        # Step 3: process the trial balances
        for trialbalance in input_data['Model']['Financials']['CustomerTrialBalance']:
            period_name = trialbalance['Period']
            self.add_period(period_name)
            for tb_entry in trialbalance['CustomerTrialBalanceItem']:
                value = float(tb_entry['DebitAmount']) - float(tb_entry['CreditAmount'])
                self.add_value(base_account_id=tb_entry['AccountId'],
                               period=period_name, value=value)

        # Step 4: process the added values to get the individual monthly values
        self.process_values(presort_names=presort_names)

        # Step 5: create the output
        financials = {
            'BalanceSheet': [],
            'IncomeStatement': []
        }
        for period in self.get_periods():
            accounts = self.get_period_normalized_values(period)
            balance_sheet = {account[0]: account[3] for account in accounts if
                             account[2] == self.BALANCE_SHEET_ACCOUNT}
            balance_sheet['Period'] = period
            income_statement = {account[0]: account[3] for account in accounts if
                                account[2] == self.INCOME_STATEMENT_ACCOUNT}
            income_statement['Period'] = period
            financials['IncomeStatement'] += [income_statement]
            financials['BalanceSheet'] += [balance_sheet]

        res = {
            'Meta': {
                'Status': 'SUCCESS',
                'DataModificationIndicator': 1,
                'Warnings': [],
            },
            'Model': {
                'Financials': financials,
                'EntityMeta': {  # TODO: what the hell is this stuff?
                    "Model": "party",
                    "SourceId": "15",
                    "SourceName": "CustomerProfile",
                    "SourceKey": "Brad7",
                    "AllSightId": "15_Brad7",
                    "Size": 89736,  # TODO: figure out what this size thing refers to
                    "Version": 17,
                    "IsDeleted": False,
                    "IsTruncated": False
                }
            }
        }

        return res
