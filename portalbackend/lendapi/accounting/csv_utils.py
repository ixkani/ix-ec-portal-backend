from portalbackend.lendapi.accounts.models import CompanyMeta
from portalbackend.lendapi.v1.accounting.utils import Utils
from .models import Company
from portalbackend.lendapi.accounting.models import TrialBalance, CoA
from portalbackend.lendapi.accounting.utils import AccountingUtils
from django.db.models import Max
from datetime import date
import calendar
import csv
import io
from django.db.models.functions import Cast
from django.db.models import IntegerField


class CSVUtils(object):
    """
    A collection of functions used in processing CSVs
    """

    @staticmethod
    def is_csv_header(line, header):
        """
        Call this function to see if the line from the file matches the expected header

        :param line:
        :param header:
        :return: boolean
        """
        is_header = True
        i = 0
        for entry in line:
            if entry != header[i]:
                is_header = False
                break
            else:
                i += 1

        return is_header

    @staticmethod
    def format_request_csv(request_csv_file):
        decoded_file = request_csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        csv_data = csv.reader(io_string, delimiter=',', quotechar='"')

        return csv_data


    @staticmethod
    def format_request_excel(data):
        from openpyxl import load_workbook
        from pandas import DataFrame
        file = data['file']
        tmpf = open('tmp.xlsx', mode='wb+')
        tmpf.write(file.read())
        wb = load_workbook(tmpf, data_only=True)
        ws = wb.active
        df = DataFrame(ws.values)
        print(df)

    @staticmethod
    def check_float_value(value):
        try:
            return float(value)
        except ValueError:
            return 0

    @staticmethod
    def file_type(data):
        # todo: this is not a reliable way to determine if it's CSV vs EXCEL, fix when we decided to accept Excel
        # This is also verified from front end with validation of file name.
        try:
            data.read().decode('utf-8')
            if ".CSV" in data.name.upper():
                return 'CSV'
            else:
                return None
        except UnicodeDecodeError:
            try:
                data.read().decode('utf-16')
                return 'Excel'
            except UnicodeDecodeError:
                return None

    @staticmethod
    def process_chart_of_accounts_csv(company, csv_data):
        # Sage
        if company.accounting_type == Company.SAGE:
            coas = []
            qbd_coa_file_header = ['', '', 'No.', 'Description', 'Type', 'Account Class']
            header_found = False

            filtered = [line for line in csv_data if len(line) > 4]
            for line in filtered:
                if len(line) != len(qbd_coa_file_header):
                    continue
                elif CSVUtils.is_csv_header(line, qbd_coa_file_header) and not header_found:
                    header_found = True
                    continue
                if (line[0] == '' and line[1] == '') or (len(line[0]) < 2 and len(line[1]) < 2):
                    i = 4
                    account_type = None
                    if len(line[4]) != 1:
                        while i < len(line):
                            if len(line[i]) == 1:
                                account_type = line[i]
                            i += 1
                    else:
                        account_type = line[4]
                        if account_type in ["A", "G"]:
                            # todo: try catch here in case of data type issue, and return errors
                            exists = CoA.objects.filter(company=company,
                                                        gl_account_id=line[2]).first()
                            if not exists:
                                c = CoA.objects.create(company=company,
                                                       gl_account_id=line[2],
                                                       gl_account_name=line[3],
                                                       gl_account_currency=company.default_currency,
                                                       gl_account_type=line[-1])
                                coas.append(c)

            if not header_found:
                return "INVALID_CSV"
            return coas

        # Quickbooks
        elif company.accounting_type == Company.QUICKBOOKS:
            coas = []
            qbd_coa_file_header = ['', 'Account', 'Type', 'Balance Total', 'Description', 'Tax Line']
            header_found = False

            for line in csv_data:
                # Only process lines which match our expected format
                if len(line) != len(qbd_coa_file_header):
                    continue
                elif CSVUtils.is_csv_header(line, qbd_coa_file_header) and not header_found:
                    header_found = True
                    continue

                exists = CoA.objects.filter(company=company,
                                            gl_account_name=line[1],
                                            gl_account_type=line[2]).first()

                if not exists:
                    # gl_account_id change made
                    c = CoA.objects.filter(company=company).annotate(gl_account_id_int=Cast('gl_account_id', IntegerField()))
                    c = c.aggregate(Max('gl_account_id_int'))

                    # Quickbooks CSV file does not send account id with the data so we need to
                    # generate our own. We try to find the last id that was set, to increment by 1
                    # from there, or set to 1 if there's no existing IDs
                    gl_acct_id = 1
                    if c['gl_account_id_int__max']:
                        gl_acct_id = int(c['gl_account_id_int__max']) + 1

                    bal = CSVUtils.check_float_value(line[3])

                    c = CoA.objects.create(company=company,
                                       gl_account_id=gl_acct_id,
                                       gl_account_name=line[1],
                                       gl_account_type=line[2],
                                       gl_account_bal=bal,
                                       gl_account_currency=company.default_currency)
                    coas.append(c)

            if not header_found:
                return "INVALID_CSV"
            return coas

    @staticmethod
    def process_canonical_coa_csv(company):
        """
        processes coa csv files in a canonical way

        :param company:
        :return:
        """
        header_dict = {
            Company.QUICKBOOKS: ['', 'Account', 'Type', 'Balance Total', 'Description', 'Tax Line'],
            Company.SAGE: ['', '', 'No.', 'Description', 'Type', 'Account Class']
        }

        # mapping is done by column index
        canonical_header_dict = {
            Company.QUICKBOOKS: {
                'gl_account_id': '',
                'gl_account_name': 1,
                'gl_account_type': 2,
                'gl_account_bal': 3
            },
            Company.SAGE: {
                'gl_account_id': 2,
                'gl_account_name': 3,
                'gl_account_type': 4,
                'gl_account_bal': ''
            },
        }

        print(header_dict[company.accounting_type])
        print(canonical_header_dict[company.accounting_type])
        return

    @staticmethod
    def process_trial_balance_csv(company, csv_data):
        # REMEMBER: when dealing with CSV files in this way, there are extra "lines" at the start of the data
        #           that contain the header.
        print('###### accounting type ', company.accounting_type)
        today = date.today()
        century = str(today.year)[:2] # QB CSV gives 2 digit year, so we append to century portion of current year.
        print('#### century is ', century)
        if company.accounting_type == Company.SAGE:
            tbs = []
            line_index = 0
            period_ending = ''
            sage_tb_file_header = ['Account Number', 'Account Description', 'Debits', 'Credits']
            header_found = False

            for line in csv_data:
                if line_index == 5:  # get period ending from file
                    try:
                        words = line[0].split(' ')
                        d = words[-1].split('/')
                        period_ending = d[2] + '-' + d[0] + '-' + d[1]

                        period = Utils.format_period(period_ending)
                        meta = CompanyMeta.objects.filter(company_id=company).first()
                        if meta.monthly_reporting_current_period != period:
                            return None

                        line_index += 1
                        continue
                    except Exception as e:
                        return "INVALID_CSV"
                elif line_index == 9:
                    line_index += 1
                    continue
                elif len(line) != len(sage_tb_file_header):
                    line_index += 1
                    continue
                elif CSVUtils.is_csv_header(line, sage_tb_file_header) and not header_found:
                    header_found = True
                    line_index += 1
                    continue
                elif len(line[1]) == 0:
                    line_index += 1
                    continue
                else:
                    print(line)

                exists = TrialBalance.objects.filter(period=period_ending, gl_account_id=line[0], company=company).first()
                if exists:
                    exists.debit = CSVUtils.check_float_value(line[2])
                    exists.credit = CSVUtils.check_float_value(line[3])
                    exists.save()
                    tbs.append(exists)
                else:
                    d = TrialBalance.objects.create(company=company, gl_account_name=line[1],
                                                    gl_account_id=line[0],
                                                    debit=CSVUtils.check_float_value(line[2]),
                                                    credit=CSVUtils.check_float_value(line[3]),
                                                    period=period_ending, currency=company.default_currency)
                    tbs.append(d)

                line_index += 1

            if not header_found:
                return "INVALID_CSV"

            return tbs

        elif company.accounting_type == Company.QUICKBOOKS:
            tbs = []
            header_found = False
            period_ending = ''

            # the first line in this file contains the period ending
            qbd_tb_file_header = ['', 'Debit', 'Credit']

            line_index = 1
            for line in csv_data:
                print('### ', line)
                if line_index == 5:
                    # QB CSV sends dates like: 30 Nov 17 ... DD MMM YY ... yuck :(
                    try:
                        period_ending = line[1].split(' ')
                        year = century+period_ending[2]
                        month_num = list(calendar.month_abbr).index(period_ending[1])
                        period_ending = year+'-'+str(month_num)+'-'+period_ending[0]

                        period = Utils.format_period(period_ending)
                        meta = CompanyMeta.objects.filter(company_id=company).first()
                        if meta.monthly_reporting_current_period != period:
                            return None

                        line_index += 1
                        continue
                    except Exception as e:
                        return "INVALID_CSV"
                # Only process lines which match our expected format
                elif len(line) != len(qbd_tb_file_header):
                    line_index += 1
                    continue
                elif CSVUtils.is_csv_header(line, qbd_tb_file_header) and not header_found:
                    header_found = True
                    line_index += 1
                    continue
                elif line[0] == 'TOTAL':
                    line_index += 1
                    continue

                gl_account_id = AccountingUtils.get_gl_account_id_by_name(company, line[0])
                print('#### TB QB glaccountid is ', gl_account_id)
                if not gl_account_id:
                    gl_account_id = 9999
                exists = TrialBalance.objects.filter(period=period_ending,
                                                     gl_account_id=gl_account_id,
                                                     company=company).first()

                print('############# checking for FLOAT ', line[1], line[2])
                if exists:
                    exists.debit = CSVUtils.check_float_value(line[1])
                    exists.credit = CSVUtils.check_float_value(line[2])
                    exists.save()
                    tbs.append(exists)
                else:
                    d = TrialBalance.objects.create(company=company,
                                                    gl_account_name=line[0],
                                                    gl_account_id=gl_account_id,
                                                    debit=CSVUtils.check_float_value(line[1]),
                                                    credit=CSVUtils.check_float_value(line[2]),
                                                    period=period_ending,
                                                    currency=company.default_currency)

                    tbs.append(d)

            line_index += 1


            if not header_found:
                return "INVALID_CSV"

            return tbs

        elif company.accounting_type == Company.XERO:
            # TODO: Handle Xero CSV Data
            pass

