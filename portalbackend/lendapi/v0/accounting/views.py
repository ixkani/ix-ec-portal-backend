from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import views


# Create your views here.
class BalanceSheetDetail(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        data = {"BalanceSheet": [{
            "Period": "2016-01",
            "TotalCurrentAssets": 32327.0,
            "TotalAssets": 35044.0,
            "TotalCurrentLiabilities": 2662.0,
            "TotalLiabilities": 27662.0,
            "TotalEquity": 7383.0,
            "TotalLiabilityAndEquity": 35045.0,
            "Cash": 24827.0,
            "AccountReceivables": 0.0,
            "SREDReceivable": 0.0,
            "OtherCurrentAssets": 7500.0,
            "FixedAssets": 2717.0,
            "PatentsAndIntangibleAssets": 0.0,
            "OtherAssets": 0.0,
            "AccountsPayableAndAccruedLiabilities": 3832.0,
            "BankDebt": 0.0,
            "OtherCurrentLiabilities": -1170.0,
            "EspressoDebtOutstanding": 0.0,
            "SeniorSecuredDebt": 0.0,
            "SubordinatedDebt": 25000.0,
            "ShareholderLoans": 0.0,
            "DeferredRevenue": 0.0,
            "OtherLiabilities": 0.0,
            "ShareAndContributedCapital": 16418.0,
            "MinorityEquityPosition": 0.0,
            "EquityPositionOfLTDebt": 0.0,
            "RetainedEarningsLoss": -2535.0,
            "NetIncomeYTD": -6500.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.549000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.549000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Period": "2016-02",
            "TotalCurrentAssets": 54453.4,
            "TotalAssets": 57103.4,
            "TotalCurrentLiabilities": 5327.4,
            "TotalLiabilities": 29573.8,
            "TotalEquity": 27529.4,
            "TotalLiabilityAndEquity": 57103.2,
            "Cash": 21568.9,
            "AccountReceivables": 24874.1,
            "SREDReceivable": 0.0,
            "OtherCurrentAssets": 8010.4,
            "FixedAssets": 2650.0,
            "PatentsAndIntangibleAssets": 0.0,
            "OtherAssets": 0.0,
            "AccountsPayableAndAccruedLiabilities": 3831.8,
            "BankDebt": 0.0,
            "OtherCurrentLiabilities": 1495.6,
            "EspressoDebtOutstanding": 0.0,
            "SeniorSecuredDebt": 0.0,
            "SubordinatedDebt": 24246.4,
            "ShareholderLoans": 0.0,
            "DeferredRevenue": 0.0,
            "OtherLiabilities": 0.0,
            "ShareAndContributedCapital": 16418.2,
            "MinorityEquityPosition": 0.0,
            "EquityPositionOfLTDebt": 0.0,
            "RetainedEarningsLoss": -2535.2,
            "NetIncomeYTD": 13646.4,
            "CreatedTimestamp": "2017-07-21 10:44:21.549000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.549000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Period": "2016-03",
            "TotalCurrentAssets": 50421.1,
            "TotalAssets": 53037.78,
            "TotalCurrentLiabilities": 3594.25,
            "TotalLiabilities": 27463.91,
            "TotalEquity": 25573.87,
            "TotalLiabilityAndEquity": 53037.78,
            "Cash": 42410.75,
            "AccountReceivables": 0.0,
            "SREDReceivable": 0.0,
            "OtherCurrentAssets": 8010.35,
            "FixedAssets": 2616.68,
            "PatentsAndIntangibleAssets": 0.0,
            "OtherAssets": 0.0,
            "AccountsPayableAndAccruedLiabilities": 3831.8,
            "BankDebt": 0.0,
            "OtherCurrentLiabilities": -237.55,
            "EspressoDebtOutstanding": 0.0,
            "SeniorSecuredDebt": 0.0,
            "SubordinatedDebt": 23869.66,
            "ShareholderLoans": 0.0,
            "DeferredRevenue": 0.0,
            "OtherLiabilities": 0.0,
            "ShareAndContributedCapital": 16418.2,
            "MinorityEquityPosition": 0.0,
            "EquityPositionOfLTDebt": 0.0,
            "RetainedEarningsLoss": -2535.19,
            "NetIncomeYTD": 11690.86,
            "CreatedTimestamp": "2017-07-21 10:44:21.549000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.549000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Period": "2016-04",
            "TotalCurrentAssets": 49928.47,
            "TotalAssets": 52511.82,
            "TotalCurrentLiabilities": 3591.86,
            "TotalLiabilities": 27084.74,
            "TotalEquity": 25427.08,
            "TotalLiabilityAndEquity": 52511.82,
            "Cash": 37752.65,
            "AccountReceivables": 4165.47,
            "SREDReceivable": 0.0,
            "OtherCurrentAssets": 8010.35,
            "FixedAssets": 2583.35,
            "PatentsAndIntangibleAssets": 0.0,
            "OtherAssets": 0.0,
            "AccountsPayableAndAccruedLiabilities": 3831.8,
            "BankDebt": 0.0,
            "OtherCurrentLiabilities": -239.94,
            "EspressoDebtOutstanding": 0.0,
            "SeniorSecuredDebt": 0.0,
            "SubordinatedDebt": 23492.88,
            "ShareholderLoans": 0.0,
            "DeferredRevenue": 0.0,
            "OtherLiabilities": 0.0,
            "ShareAndContributedCapital": 16418.2,
            "MinorityEquityPosition": 0.0,
            "EquityPositionOfLTDebt": 0.0,
            "RetainedEarningsLoss": -2535.19,
            "NetIncomeYTD": 11544.07,
            "CreatedTimestamp": "2017-07-21 10:44:21.549000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.549000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Period": "2016-05",
            "TotalCurrentAssets": 54869.85,
            "TotalAssets": 57419.87,
            "TotalCurrentLiabilities": 4268.89,
            "TotalLiabilities": 27008.21,
            "TotalEquity": 30411.66,
            "TotalLiabilityAndEquity": 57419.87,
            "Cash": 34291.06,
            "AccountReceivables": 12568.44,
            "SREDReceivable": 0.0,
            "OtherCurrentAssets": 8010.35,
            "FixedAssets": 2550.02,
            "PatentsAndIntangibleAssets": 0.0,
            "OtherAssets": 0.0,
            "AccountsPayableAndAccruedLiabilities": 3831.8,
            "BankDebt": 0.0,
            "OtherCurrentLiabilities": 437.09,
            "EspressoDebtOutstanding": 0.0,
            "SeniorSecuredDebt": 0.0,
            "SubordinatedDebt": 22739.32,
            "ShareholderLoans": 0.0,
            "DeferredRevenue": 0.0,
            "OtherLiabilities": 0.0,
            "ShareAndContributedCapital": 16418.2,
            "MinorityEquityPosition": 0.0,
            "EquityPositionOfLTDebt": 0.0,
            "RetainedEarningsLoss": -2535.19,
            "NetIncomeYTD": 16528.65,
            "CreatedTimestamp": "2017-07-21 10:44:21.549000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.549000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Period": "2016-06",
            "TotalCurrentAssets": 46406.13,
            "TotalAssets": 48922.82,
            "TotalCurrentLiabilities": 3349.46,
            "TotalLiabilities": 25712.0,
            "TotalEquity": 23210.82,
            "TotalLiabilityAndEquity": 48922.82,
            "Cash": 38850.61,
            "AccountReceivables": -454.83,
            "SREDReceivable": 0.0,
            "OtherCurrentAssets": 8010.35,
            "FixedAssets": 2516.69,
            "PatentsAndIntangibleAssets": 0.0,
            "OtherAssets": 0.0,
            "AccountsPayableAndAccruedLiabilities": 3831.8,
            "BankDebt": 0.0,
            "OtherCurrentLiabilities": -482.34,
            "EspressoDebtOutstanding": 0.0,
            "SeniorSecuredDebt": 0.0,
            "SubordinatedDebt": 22362.54,
            "ShareholderLoans": 0.0,
            "DeferredRevenue": 0.0,
            "OtherLiabilities": 0.0,
            "ShareAndContributedCapital": 16418.2,
            "MinorityEquityPosition": 0.0,
            "EquityPositionOfLTDebt": 0.0,
            "RetainedEarningsLoss": -2535.19,
            "NetIncomeYTD": 9327.81,
            "CreatedTimestamp": "2017-07-21 10:44:21.549000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.549000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Period": "2016-07",
            "TotalCurrentAssets": 53561.87,
            "TotalAssets": 56045.23,
            "TotalCurrentLiabilities": 4226.97,
            "TotalLiabilities": 26212.73,
            "TotalEquity": 29832.5,
            "TotalLiabilityAndEquity": 56045.23,
            "Cash": 46006.35,
            "AccountReceivables": -454.83,
            "SREDReceivable": 0.0,
            "OtherCurrentAssets": 8010.35,
            "FixedAssets": 2483.36,
            "PatentsAndIntangibleAssets": 0.0,
            "OtherAssets": 0.0,
            "AccountsPayableAndAccruedLiabilities": 3831.8,
            "BankDebt": 0.0,
            "OtherCurrentLiabilities": 395.17,
            "EspressoDebtOutstanding": 0.0,
            "SeniorSecuredDebt": 0.0,
            "SubordinatedDebt": 21985.76,
            "ShareholderLoans": 0.0,
            "DeferredRevenue": 0.0,
            "OtherLiabilities": 0.0,
            "ShareAndContributedCapital": 16418.2,
            "MinorityEquityPosition": 0.0,
            "EquityPositionOfLTDebt": 0.0,
            "RetainedEarningsLoss": -2535.19,
            "NetIncomeYTD": 15949.49,
            "CreatedTimestamp": "2017-07-21 10:44:21.549000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.549000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Period": "2016-08",
            "TotalCurrentAssets": 53019.24,
            "TotalAssets": 55469.27,
            "TotalCurrentLiabilities": 3551.38,
            "TotalLiabilities": 25160.36,
            "TotalEquity": 30308.91,
            "TotalLiabilityAndEquity": 55469.27,
            "Cash": 37022.62,
            "AccountReceivables": 7986.27,
            "SREDReceivable": 0.0,
            "OtherCurrentAssets": 8010.35,
            "FixedAssets": 2450.03,
            "PatentsAndIntangibleAssets": 0.0,
            "OtherAssets": 0.0,
            "AccountsPayableAndAccruedLiabilities": 3077.6,
            "BankDebt": 0.0,
            "OtherCurrentLiabilities": 473.78,
            "EspressoDebtOutstanding": 0.0,
            "SeniorSecuredDebt": 0.0,
            "SubordinatedDebt": 21608.98,
            "ShareholderLoans": 0.0,
            "DeferredRevenue": 0.0,
            "OtherLiabilities": 0.0,
            "ShareAndContributedCapital": 16418.2,
            "MinorityEquityPosition": 0.0,
            "EquityPositionOfLTDebt": 0.0,
            "RetainedEarningsLoss": -2535.19,
            "NetIncomeYTD": 16425.9,
            "CreatedTimestamp": "2017-07-21 10:44:21.549000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.549000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Period": "2016-09",
            "TotalCurrentAssets": 51412.01,
            "TotalAssets": 53828.71,
            "TotalCurrentLiabilities": 3677.44,
            "TotalLiabilities": 24532.86,
            "TotalEquity": 29295.85,
            "TotalLiabilityAndEquity": 53828.71,
            "Cash": 39883.86,
            "AccountReceivables": 6819.54,
            "SREDReceivable": 0.0,
            "OtherCurrentAssets": 4708.61,
            "FixedAssets": 2416.7,
            "PatentsAndIntangibleAssets": 0.0,
            "OtherAssets": 0.0,
            "AccountsPayableAndAccruedLiabilities": 2812.11,
            "BankDebt": 0.0,
            "OtherCurrentLiabilities": 865.33,
            "EspressoDebtOutstanding": 0.0,
            "SeniorSecuredDebt": 0.0,
            "SubordinatedDebt": 20855.42,
            "ShareholderLoans": 0.0,
            "DeferredRevenue": 0.0,
            "OtherLiabilities": 0.0,
            "ShareAndContributedCapital": 15918.2,
            "MinorityEquityPosition": 0.0,
            "EquityPositionOfLTDebt": 0.0,
            "RetainedEarningsLoss": -2535.19,
            "NetIncomeYTD": 15912.84,
            "CreatedTimestamp": "2017-07-21 10:44:21.549000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.549000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Period": "2016-10",
            "TotalCurrentAssets": 46206.57,
            "TotalAssets": 48589.94,
            "TotalCurrentLiabilities": 2666.43,
            "TotalLiabilities": 23145.07,
            "TotalEquity": 25444.87,
            "TotalLiabilityAndEquity": 48589.94,
            "Cash": 18041.58,
            "AccountReceivables": 18402.04,
            "SREDReceivable": 0.0,
            "OtherCurrentAssets": 9762.95,
            "FixedAssets": 2383.37,
            "PatentsAndIntangibleAssets": 0.0,
            "OtherAssets": 0.0,
            "AccountsPayableAndAccruedLiabilities": 2812.11,
            "BankDebt": 0.0,
            "OtherCurrentLiabilities": -145.68,
            "EspressoDebtOutstanding": 0.0,
            "SeniorSecuredDebt": 0.0,
            "SubordinatedDebt": 20478.64,
            "ShareholderLoans": 0.0,
            "DeferredRevenue": 0.0,
            "OtherLiabilities": 0.0,
            "ShareAndContributedCapital": 14918.2,
            "MinorityEquityPosition": 0.0,
            "EquityPositionOfLTDebt": 0.0,
            "RetainedEarningsLoss": 6901.05,
            "NetIncomeYTD": 3625.62,
            "CreatedTimestamp": "2017-07-21 10:44:21.549000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.549000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Period": "2016-11",
            "TotalCurrentAssets": 47279.52,
            "TotalAssets": 49662.89,
            "TotalCurrentLiabilities": 3129.57,
            "TotalLiabilities": 23231.43,
            "TotalEquity": 26431.46,
            "TotalLiabilityAndEquity": 49662.89,
            "Cash": 21095.57,
            "AccountReceivables": 18402.04,
            "SREDReceivable": 0.0,
            "OtherCurrentAssets": 7781.91,
            "FixedAssets": 2383.37,
            "PatentsAndIntangibleAssets": 0.0,
            "OtherAssets": 0.0,
            "AccountsPayableAndAccruedLiabilities": 2812.11,
            "BankDebt": 0.0,
            "OtherCurrentLiabilities": 317.46,
            "EspressoDebtOutstanding": 0.0,
            "SeniorSecuredDebt": 0.0,
            "SubordinatedDebt": 20101.86,
            "ShareholderLoans": 0.0,
            "DeferredRevenue": 0.0,
            "OtherLiabilities": 0.0,
            "ShareAndContributedCapital": 10750.0,
            "MinorityEquityPosition": 0.0,
            "EquityPositionOfLTDebt": 0.0,
            "RetainedEarningsLoss": 10569.25,
            "NetIncomeYTD": 5112.21,
            "CreatedTimestamp": "2017-07-21 10:44:21.549000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.549000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Period": "2016-12",
            "TotalCurrentAssets": 47279.52,
            "TotalAssets": 49662.89,
            "TotalCurrentLiabilities": 3129.57,
            "TotalLiabilities": 23231.43,
            "TotalEquity": 26431.46,
            "TotalLiabilityAndEquity": 49662.89,
            "Cash": 21095.57,
            "AccountReceivables": 18402.04,
            "SREDReceivable": 0.0,
            "OtherCurrentAssets": 7781.91,
            "FixedAssets": 2383.37,
            "PatentsAndIntangibleAssets": 0.0,
            "OtherAssets": 0.0,
            "AccountsPayableAndAccruedLiabilities": 2812.11,
            "BankDebt": 0.0,
            "OtherCurrentLiabilities": 317.46,
            "EspressoDebtOutstanding": 0.0,
            "SeniorSecuredDebt": 0.0,
            "SubordinatedDebt": 20101.86,
            "ShareholderLoans": 0.0,
            "DeferredRevenue": 0.0,
            "OtherLiabilities": 0.0,
            "ShareAndContributedCapital": 10750.0,
            "MinorityEquityPosition": 0.0,
            "EquityPositionOfLTDebt": 0.0,
            "RetainedEarningsLoss": 10569.25,
            "NetIncomeYTD": 5112.21,
            "CreatedTimestamp": "2017-07-21 10:44:21.549000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.549000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Period": "2017-01",
            "TotalCurrentAssets": 47279.52,
            "TotalAssets": 49662.89,
            "TotalCurrentLiabilities": 3129.57,
            "TotalLiabilities": 23231.43,
            "TotalEquity": 26431.46,
            "TotalLiabilityAndEquity": 49662.89,
            "Cash": 21095.57,
            "AccountReceivables": 18402.04,
            "SREDReceivable": 0.0,
            "OtherCurrentAssets": 7781.91,
            "FixedAssets": 2383.37,
            "PatentsAndIntangibleAssets": 0.0,
            "OtherAssets": 0.0,
            "AccountsPayableAndAccruedLiabilities": 2812.11,
            "BankDebt": 0.0,
            "OtherCurrentLiabilities": 317.46,
            "EspressoDebtOutstanding": 0.0,
            "SeniorSecuredDebt": 0.0,
            "SubordinatedDebt": 20101.86,
            "ShareholderLoans": 0.0,
            "DeferredRevenue": 0.0,
            "OtherLiabilities": 0.0,
            "ShareAndContributedCapital": 10750.0,
            "MinorityEquityPosition": 0.0,
            "EquityPositionOfLTDebt": 0.0,
            "RetainedEarningsLoss": 15681.46,
            "NetIncomeYTD": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.549000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.549000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }
        ]}
        return Response(data)


class CoaMapDetail(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        data = {"CustomerAccountMapping": [{
            "FromAccountName": "Insurance",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Exchange Gain or Loss",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Utilities",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Venue Fees paid on behalf of clients",
            "ToAccountName": "Cost of Goods Sold",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Accounts Receivable",
            "ToAccountName": "Accounts Receivables",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Promotional",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Advertising",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Travel",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Markup",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Entertainment Booking Fees paid on behalf of clients",
            "ToAccountName": "Cost of Goods Sold",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Opening Balance Equity",
            "ToAccountName": "Share Capital and Contributed Capital",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Undeposited Funds",
            "ToAccountName": "Other Current Assets",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Accounts Payable (A/P) - HKD",
            "ToAccountName": "Accounts Payable and Accrued Liabilities",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Printed Materials purchased for clients",
            "ToAccountName": "Cost of Goods Sold",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Travel Expense",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Sales of Product Income",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Owner\u0027s Equity - Contributions",
            "ToAccountName": "Share Capital and Contributed Capital",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "GST/HST Payable",
            "ToAccountName": "Other Current Liabilities",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Sales Discounts",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Printing and Reproduction",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Fees Billed",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Rent or lease payments",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Chequing",
            "ToAccountName": "Cash",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Office expenses",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Billable Expense Income",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Charitable Contributions",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Accumulated Depreciation",
            "ToAccountName": "Fixed Assets",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Telephone Expense",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Commissions and fees",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Vehicles",
            "ToAccountName": "Fixed Assets",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Meals and entertainment",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Insurance Expense-General Liability Insurance",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Penalties and settlements",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Insurance Expense",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Refunds-Allowances",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Inventory Shrinkage",
            "ToAccountName": "Cost of Goods Sold",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Uncategorised Income",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Commission Income",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Interest expense",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Cost of Sales - billable expenses",
            "ToAccountName": "Cost of Goods Sold",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Leasehold Improvements",
            "ToAccountName": "Fixed Assets",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Billable Expenses Income",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Bank charges",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Cost of sales",
            "ToAccountName": "Cost of Goods Sold",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Depreciation Expense",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Owner\u0027s Equity",
            "ToAccountName": "Share Capital and Contributed Capital",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Discounts given",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Sales",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Visa Credit Card",
            "ToAccountName": "Accounts Payable and Accrued Liabilities",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Utilities - Electric \u0026 Gas",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Travel meals",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Miscellaneous",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Inventory Asset",
            "ToAccountName": "Other Current Assets",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Commissions Paid",
            "ToAccountName": "Cost of Goods Sold",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Insurance Expense-Life and Disability Insurance",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Accounts Payable",
            "ToAccountName": "Accounts Payable and Accrued Liabilities",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Purchases",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Repair and maintenance",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Uncategorized Asset",
            "ToAccountName": "Other Current Assets",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Equipment rental",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Business Licenses and Permits",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Stationery and printing",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Merchant Account Fees",
            "ToAccountName": "Cost of Goods Sold",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Uncategorised Expense",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Rent Expense",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Continuing Education",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Accounts Receivable (A/R) - USD",
            "ToAccountName": "Accounts Receivables",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Utilities - Water",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Supplies",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Uncategorized Income",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Dues and Subscriptions",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Ask My Accountant",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Prepaid expenses",
            "ToAccountName": "Other Current Assets",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Note Payable",
            "ToAccountName": "Subordinated Debt (to Espresso)",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Janitorial Expense",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Cost of Goods Sold",
            "ToAccountName": "Cost of Goods Sold",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "GST/HST Suspense",
            "ToAccountName": "Other Current Liabilities",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Subcontracted Services",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Owner\u0027s Equity - Draws",
            "ToAccountName": "Share Capital and Contributed Capital",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Other Portfolio Income",
            "ToAccountName": "Other Income (Expenses)",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Furniture and Equipment",
            "ToAccountName": "Fixed Assets",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Uncategorized Expense",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Taxes - Property",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Unapplied Cash Payment Income",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Taxes and Licenses",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Services",
            "ToAccountName": "Non-Recurring Revenues",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Uncategorised Asset",
            "ToAccountName": "Other Current Assets",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Insurance Expense-Health Insurance",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Computer and Internet Expenses",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Interest earned",
            "ToAccountName": "Other Income (Expenses)",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Professional Fees",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Unapplied Cash Bill Payment Expense",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Legal and professional fees",
            "ToAccountName": "G\u0026A",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "FromAccountName": "Retained Earnings",
            "ToAccountName": "Retained Earnings (Loss)",
            "CreatedTimestamp": "2017-07-21 10:39:30.111000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.550000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }]}
        return Response(data)


class IncomeStatementDetail(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        data= {"IncomeStatement": [{
            "Ebitda": -6500.0,
            "NetIncome": -6500.0,
            "Period": "2016-01",
            "TotalRevenue": 0.0,
            "GrossProfit": -5000.0,
            "NonRecurringRevenues": 0.0,
            "RecurringRevenues": 0.0,
            "CostOfGoodsSold": 5000.0,
            "SalesAndMarketingExpenses": 0.0,
            "RDGrossMinusExcludingSRED": 0.0,
            "GA": 1500.0,
            "InterestIncomeExpense": 0.0,
            "SREDAccrual": 0.0,
            "IRAPGrantsReceived": 0.0,
            "DepreciationAndAmortization": 0.0,
            "OtherIncomeExpenses": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.547000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.547000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Ebitda": 20146.4,
            "NetIncome": 20146.4,
            "Period": "2016-02",
            "TotalRevenue": 22012.5,
            "GrossProfit": 21927.5,
            "NonRecurringRevenues": 22012.5,
            "RecurringRevenues": 0.0,
            "CostOfGoodsSold": 85.0,
            "SalesAndMarketingExpenses": 0.0,
            "RDGrossMinusExcludingSRED": 0.0,
            "GA": 1781.1,
            "InterestIncomeExpense": 0.0,
            "SREDAccrual": 0.0,
            "IRAPGrantsReceived": 0.0,
            "DepreciationAndAmortization": 0.0,
            "OtherIncomeExpenses": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.547000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.547000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Ebitda": -1955.54,
            "NetIncome": -1955.54,
            "Period": "2016-03",
            "TotalRevenue": 0.0,
            "GrossProfit": -273.74,
            "NonRecurringRevenues": 0.0,
            "RecurringRevenues": 0.0,
            "CostOfGoodsSold": 273.74,
            "SalesAndMarketingExpenses": 0.0,
            "RDGrossMinusExcludingSRED": 0.0,
            "GA": 1681.8,
            "InterestIncomeExpense": 0.0,
            "SREDAccrual": 0.0,
            "IRAPGrantsReceived": 0.0,
            "DepreciationAndAmortization": 0.0,
            "OtherIncomeExpenses": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.547000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.547000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Ebitda": -146.79,
            "NetIncome": -146.79,
            "Period": "2016-04",
            "TotalRevenue": 3686.25,
            "GrossProfit": 2236.25,
            "NonRecurringRevenues": 3686.25,
            "RecurringRevenues": 0.0,
            "CostOfGoodsSold": 1450.0,
            "SalesAndMarketingExpenses": 0.0,
            "RDGrossMinusExcludingSRED": 0.0,
            "GA": 2383.04,
            "InterestIncomeExpense": 0.0,
            "SREDAccrual": 0.0,
            "IRAPGrantsReceived": 0.0,
            "DepreciationAndAmortization": 0.0,
            "OtherIncomeExpenses": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.547000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.547000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Ebitda": 4984.58,
            "NetIncome": 4984.58,
            "Period": "2016-05",
            "TotalRevenue": 11122.5,
            "GrossProfit": 6825.5,
            "NonRecurringRevenues": 11122.5,
            "RecurringRevenues": 0.0,
            "CostOfGoodsSold": 4297.0,
            "SalesAndMarketingExpenses": 0.0,
            "RDGrossMinusExcludingSRED": 0.0,
            "GA": 1840.92,
            "InterestIncomeExpense": 0.0,
            "SREDAccrual": 0.0,
            "IRAPGrantsReceived": 0.0,
            "DepreciationAndAmortization": 0.0,
            "OtherIncomeExpenses": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.547000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.547000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Ebitda": -7200.84,
            "NetIncome": -7200.84,
            "Period": "2016-06",
            "TotalRevenue": 0.0,
            "GrossProfit": -5491.5,
            "NonRecurringRevenues": 0.0,
            "RecurringRevenues": 0.0,
            "CostOfGoodsSold": 5491.5,
            "SalesAndMarketingExpenses": 0.0,
            "RDGrossMinusExcludingSRED": 0.0,
            "GA": 1709.34,
            "InterestIncomeExpense": 0.0,
            "SREDAccrual": 0.0,
            "IRAPGrantsReceived": 0.0,
            "DepreciationAndAmortization": 0.0,
            "OtherIncomeExpenses": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.547000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.547000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Ebitda": 6621.68,
            "NetIncome": 6621.68,
            "Period": "2016-07",
            "TotalRevenue": 9049.8,
            "GrossProfit": 9049.8,
            "NonRecurringRevenues": 9049.8,
            "RecurringRevenues": 0.0,
            "CostOfGoodsSold": 0.0,
            "SalesAndMarketingExpenses": 0.0,
            "RDGrossMinusExcludingSRED": 0.0,
            "GA": 2428.12,
            "InterestIncomeExpense": 0.0,
            "SREDAccrual": 0.0,
            "IRAPGrantsReceived": 0.0,
            "DepreciationAndAmortization": 0.0,
            "OtherIncomeExpenses": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.547000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.547000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Ebitda": 476.41,
            "NetIncome": 476.41,
            "Period": "2016-08",
            "TotalRevenue": 7470.0,
            "GrossProfit": 2351.25,
            "NonRecurringRevenues": 7470.0,
            "RecurringRevenues": 0.0,
            "CostOfGoodsSold": 5118.75,
            "SalesAndMarketingExpenses": 0.0,
            "RDGrossMinusExcludingSRED": 0.0,
            "GA": 1874.84,
            "InterestIncomeExpense": 0.0,
            "SREDAccrual": 0.0,
            "IRAPGrantsReceived": 0.0,
            "DepreciationAndAmortization": 0.0,
            "OtherIncomeExpenses": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.547000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.547000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Ebitda": -513.06,
            "NetIncome": -513.06,
            "Period": "2016-09",
            "TotalRevenue": 7300.0,
            "GrossProfit": 1360.76,
            "NonRecurringRevenues": 7300.0,
            "RecurringRevenues": 0.0,
            "CostOfGoodsSold": 5939.24,
            "SalesAndMarketingExpenses": 0.0,
            "RDGrossMinusExcludingSRED": 0.0,
            "GA": 1873.82,
            "InterestIncomeExpense": 0.0,
            "SREDAccrual": 0.0,
            "IRAPGrantsReceived": 0.0,
            "DepreciationAndAmortization": 0.0,
            "OtherIncomeExpenses": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.547000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.547000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Ebitda": -12287.22,
            "NetIncome": -12287.22,
            "Period": "2016-10",
            "TotalRevenue": 10250.0,
            "GrossProfit": -9881.9,
            "NonRecurringRevenues": 10250.0,
            "RecurringRevenues": 0.0,
            "CostOfGoodsSold": 20131.9,
            "SalesAndMarketingExpenses": 0.0,
            "RDGrossMinusExcludingSRED": 0.0,
            "GA": 2405.32,
            "InterestIncomeExpense": 0.0,
            "SREDAccrual": 0.0,
            "IRAPGrantsReceived": 0.0,
            "DepreciationAndAmortization": 0.0,
            "OtherIncomeExpenses": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.547000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.547000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Ebitda": 1486.59,
            "NetIncome": 1486.59,
            "Period": "2016-11",
            "TotalRevenue": 5100.0,
            "GrossProfit": 3118.96,
            "NonRecurringRevenues": 5100.0,
            "RecurringRevenues": 0.0,
            "CostOfGoodsSold": 1981.04,
            "SalesAndMarketingExpenses": 0.0,
            "RDGrossMinusExcludingSRED": 0.0,
            "GA": 1632.37,
            "InterestIncomeExpense": 0.0,
            "SREDAccrual": 0.0,
            "IRAPGrantsReceived": 0.0,
            "DepreciationAndAmortization": 0.0,
            "OtherIncomeExpenses": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.547000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.547000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Ebitda": 0.0,
            "NetIncome": 0.0,
            "Period": "2016-12",
            "TotalRevenue": 0.0,
            "GrossProfit": 0.0,
            "NonRecurringRevenues": 0.0,
            "RecurringRevenues": 0.0,
            "CostOfGoodsSold": 0.0,
            "SalesAndMarketingExpenses": 0.0,
            "RDGrossMinusExcludingSRED": 0.0,
            "GA": 0.0,
            "InterestIncomeExpense": 0.0,
            "SREDAccrual": 0.0,
            "IRAPGrantsReceived": 0.0,
            "DepreciationAndAmortization": 0.0,
            "OtherIncomeExpenses": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.547000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.547000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Ebitda": 0.0,
            "NetIncome": 0.0,
            "Period": "2017-01",
            "TotalRevenue": 0.0,
            "GrossProfit": 0.0,
            "NonRecurringRevenues": 0.0,
            "RecurringRevenues": 0.0,
            "CostOfGoodsSold": 0.0,
            "SalesAndMarketingExpenses": 0.0,
            "RDGrossMinusExcludingSRED": 0.0,
            "GA": 0.0,
            "InterestIncomeExpense": 0.0,
            "SREDAccrual": 0.0,
            "IRAPGrantsReceived": 0.0,
            "DepreciationAndAmortization": 0.0,
            "OtherIncomeExpenses": 0.0,
            "CreatedTimestamp": "2017-07-21 10:44:21.547000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.547000",
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }]}
        return Response(data)


class TrialBalanceDetail(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        data = {"CustomerTrialBalance": [{
            "Version": "1",
            "Period": "2016-01",
            "RecordedTimestamp": "2017-07-21 10:44:20.468000",
            "CustomerTrialBalanceItem": [{
                "AccountName": "Accounts Payable",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Payable (A/P) - HKD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable (A/R) - USD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accumulated Depreciation",
                "DebitAmount": -33.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Advertising",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Ask My Accountant",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Bank charges",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expense Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expenses Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Business Licenses and Permits",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Charitable Contributions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Chequing",
                "DebitAmount": 24827.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commission Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions and fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions Paid",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Computer and Internet Expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Continuing Education",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Goods Sold",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Sales - billable expenses",
                "DebitAmount": 5000.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Depreciation Expense",
                "DebitAmount": 33.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Discounts given",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Dues and Subscriptions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Entertainment Booking Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Equipment rental",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Exchange Gain or Loss",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Fees Billed",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Furniture and Equipment",
                "DebitAmount": 2750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Payable",
                "DebitAmount": 1170.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Suspense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-General Liability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Health Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Life and Disability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest earned",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Asset",
                "DebitAmount": 7500.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Shrinkage",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Janitorial Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Leasehold Improvements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Legal and professional fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Markup",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Meals and entertainment",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Merchant Account Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Miscellaneous",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Note Payable",
                "DebitAmount": -25000.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Office expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Opening Balance Equity",
                "DebitAmount": -3668.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Other Portfolio Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Contributions",
                "DebitAmount": -12750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Draws",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Penalties and settlements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Prepaid expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printed Materials purchased for clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printing and Reproduction",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Professional Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Promotional",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Purchases",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Refunds-Allowances",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent Expense",
                "DebitAmount": 1250.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent or lease payments",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Repair and maintenance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Retained Earnings",
                "DebitAmount": 2535.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales Discounts",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales of Product Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Stationery and printing",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Subcontracted Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Supplies",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes - Property",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes and Licenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Telephone Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel meals",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Bill Payment Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Payment Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Undeposited Funds",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Electric \u0026 Gas",
                "DebitAmount": 166.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Water",
                "DebitAmount": 51.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Vehicles",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Venue Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Visa Credit Card",
                "DebitAmount": -3832.0,
                "CreditAmount": 0.0,
                "Quality": []
            }
            ],
            "CreatedTimestamp": "2017-07-21 10:44:21.544000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.544000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Version": "1",
            "Period": "2016-02",
            "RecordedTimestamp": "2017-07-21 10:44:20.468000",
            "CustomerTrialBalanceItem": [{
                "AccountName": "Accounts Payable",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Payable (A/P) - HKD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable",
                "DebitAmount": 24874.1,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable (A/R) - USD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accumulated Depreciation",
                "DebitAmount": -100.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Advertising",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Ask My Accountant",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Bank charges",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expense Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expenses Income",
                "DebitAmount": -17012.5,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Business Licenses and Permits",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Charitable Contributions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Chequing",
                "DebitAmount": 21568.9,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commission Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions and fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions Paid",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Computer and Internet Expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Continuing Education",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Goods Sold",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Sales - billable expenses",
                "DebitAmount": 5085.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Depreciation Expense",
                "DebitAmount": 100.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Discounts given",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Dues and Subscriptions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Entertainment Booking Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Equipment rental",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Exchange Gain or Loss",
                "DebitAmount": 18.4,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Fees Billed",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Furniture and Equipment",
                "DebitAmount": 2750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Payable",
                "DebitAmount": -1495.6,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Suspense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-General Liability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Health Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Life and Disability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest earned",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest expense",
                "DebitAmount": 190.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Asset",
                "DebitAmount": 8010.4,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Shrinkage",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Janitorial Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Leasehold Improvements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Legal and professional fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Markup",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Meals and entertainment",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Merchant Account Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Miscellaneous",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Note Payable",
                "DebitAmount": -24246.4,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Office expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Opening Balance Equity",
                "DebitAmount": -3668.2,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Other Portfolio Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Contributions",
                "DebitAmount": -12750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Draws",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Penalties and settlements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Prepaid expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printed Materials purchased for clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printing and Reproduction",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Professional Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Promotional",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Purchases",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Refunds-Allowances",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent Expense",
                "DebitAmount": 2500.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent or lease payments",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Repair and maintenance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Retained Earnings",
                "DebitAmount": 2535.2,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales",
                "DebitAmount": -5000.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales Discounts",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales of Product Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Stationery and printing",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Subcontracted Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Supplies",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes - Property",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes and Licenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Telephone Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel meals",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Bill Payment Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Payment Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Undeposited Funds",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Electric \u0026 Gas",
                "DebitAmount": 352.7,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Water",
                "DebitAmount": 120.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Vehicles",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Venue Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Visa Credit Card",
                "DebitAmount": -3831.8,
                "CreditAmount": 0.0,
                "Quality": []
            }
            ],
            "CreatedTimestamp": "2017-07-21 10:44:21.544000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.544000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Version": "1",
            "Period": "2016-03",
            "RecordedTimestamp": "2017-07-21 10:44:20.468000",
            "CustomerTrialBalanceItem": [{
                "AccountName": "Accounts Payable",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Payable (A/P) - HKD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable (A/R) - USD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accumulated Depreciation",
                "DebitAmount": -133.32,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Advertising",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Ask My Accountant",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Bank charges",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expense Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expenses Income",
                "DebitAmount": -17012.5,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Business Licenses and Permits",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Charitable Contributions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Chequing",
                "DebitAmount": 42410.75,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commission Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions and fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions Paid",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Computer and Internet Expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Continuing Education",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Goods Sold",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Sales - billable expenses",
                "DebitAmount": 5358.74,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Depreciation Expense",
                "DebitAmount": 133.32,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Discounts given",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Dues and Subscriptions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Entertainment Booking Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Equipment rental",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Exchange Gain or Loss",
                "DebitAmount": 18.36,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Fees Billed",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Furniture and Equipment",
                "DebitAmount": 2750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Payable",
                "DebitAmount": -1258.07,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Suspense",
                "DebitAmount": 1495.62,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-General Liability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Health Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Life and Disability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest earned",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest expense",
                "DebitAmount": 285.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Asset",
                "DebitAmount": 8010.35,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Shrinkage",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Janitorial Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Leasehold Improvements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Legal and professional fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Markup",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Meals and entertainment",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Merchant Account Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Miscellaneous",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Note Payable",
                "DebitAmount": -23869.66,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Office expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Opening Balance Equity",
                "DebitAmount": -3668.2,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Other Portfolio Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Contributions",
                "DebitAmount": -12750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Draws",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Penalties and settlements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Prepaid expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printed Materials purchased for clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printing and Reproduction",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Professional Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Promotional",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Purchases",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Refunds-Allowances",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent Expense",
                "DebitAmount": 3750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent or lease payments",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Repair and maintenance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Retained Earnings",
                "DebitAmount": 2535.19,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales",
                "DebitAmount": -5000.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales Discounts",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales of Product Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Stationery and printing",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Subcontracted Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Supplies",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes - Property",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes and Licenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Telephone Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel meals",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Bill Payment Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Payment Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Undeposited Funds",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Electric \u0026 Gas",
                "DebitAmount": 567.53,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Water",
                "DebitAmount": 208.69,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Vehicles",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Venue Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Visa Credit Card",
                "DebitAmount": -3831.8,
                "CreditAmount": 0.0,
                "Quality": []
            }
            ],
            "CreatedTimestamp": "2017-07-21 10:44:21.544000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.544000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Version": "1",
            "Period": "2016-04",
            "RecordedTimestamp": "2017-07-21 10:44:20.468000",
            "CustomerTrialBalanceItem": [{
                "AccountName": "Accounts Payable",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Payable (A/P) - HKD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable",
                "DebitAmount": 4165.47,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable (A/R) - USD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accumulated Depreciation",
                "DebitAmount": -166.65,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Advertising",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Ask My Accountant",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Bank charges",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expense Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expenses Income",
                "DebitAmount": -18736.25,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Business Licenses and Permits",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Charitable Contributions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Chequing",
                "DebitAmount": 37752.65,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commission Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions and fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions Paid",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Computer and Internet Expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Continuing Education",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Goods Sold",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Sales - billable expenses",
                "DebitAmount": 6808.74,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Depreciation Expense",
                "DebitAmount": 166.65,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Discounts given",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Dues and Subscriptions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Entertainment Booking Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Equipment rental",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Exchange Gain or Loss",
                "DebitAmount": 18.36,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Fees Billed",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Furniture and Equipment",
                "DebitAmount": 2750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Payable",
                "DebitAmount": -1255.68,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Suspense",
                "DebitAmount": 1495.62,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-General Liability Insurance",
                "DebitAmount": 750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Health Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Life and Disability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest earned",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest expense",
                "DebitAmount": 380.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Asset",
                "DebitAmount": 8010.35,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Shrinkage",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Janitorial Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Leasehold Improvements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Legal and professional fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Markup",
                "DebitAmount": -462.5,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Meals and entertainment",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Merchant Account Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Miscellaneous",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Note Payable",
                "DebitAmount": -23492.88,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Office expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Opening Balance Equity",
                "DebitAmount": -3668.2,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Other Portfolio Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Contributions",
                "DebitAmount": -12750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Draws",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Penalties and settlements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Prepaid expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printed Materials purchased for clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printing and Reproduction",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Professional Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Promotional",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Purchases",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Refunds-Allowances",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent Expense",
                "DebitAmount": 5000.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent or lease payments",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Repair and maintenance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Retained Earnings",
                "DebitAmount": 2535.19,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales",
                "DebitAmount": -6500.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales Discounts",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales of Product Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Stationery and printing",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Subcontracted Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Supplies",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes - Property",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes and Licenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Telephone Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel meals",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Bill Payment Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Payment Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Undeposited Funds",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Electric \u0026 Gas",
                "DebitAmount": 822.24,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Water",
                "DebitAmount": 208.69,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Vehicles",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Venue Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Visa Credit Card",
                "DebitAmount": -3831.8,
                "CreditAmount": 0.0,
                "Quality": []
            }
            ],
            "CreatedTimestamp": "2017-07-21 10:44:21.544000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.544000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Version": "1",
            "Period": "2016-05",
            "RecordedTimestamp": "2017-07-21 10:44:20.468000",
            "CustomerTrialBalanceItem": [{
                "AccountName": "Accounts Payable",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Payable (A/P) - HKD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable",
                "DebitAmount": 12568.44,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable (A/R) - USD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accumulated Depreciation",
                "DebitAmount": -199.98,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Advertising",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Ask My Accountant",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Bank charges",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expense Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expenses Income",
                "DebitAmount": -23033.25,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Business Licenses and Permits",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Charitable Contributions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Chequing",
                "DebitAmount": 34291.06,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commission Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions and fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions Paid",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Computer and Internet Expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Continuing Education",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Goods Sold",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Sales - billable expenses",
                "DebitAmount": 11105.74,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Depreciation Expense",
                "DebitAmount": 199.98,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Discounts given",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Dues and Subscriptions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Entertainment Booking Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Equipment rental",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Exchange Gain or Loss",
                "DebitAmount": 18.36,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Fees Billed",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Furniture and Equipment",
                "DebitAmount": 2750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Payable",
                "DebitAmount": -1932.71,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Suspense",
                "DebitAmount": 1495.62,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-General Liability Insurance",
                "DebitAmount": 750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Health Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Life and Disability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest earned",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest expense",
                "DebitAmount": 570.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Asset",
                "DebitAmount": 8010.35,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Shrinkage",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Janitorial Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Leasehold Improvements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Legal and professional fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Markup",
                "DebitAmount": -1538.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Meals and entertainment",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Merchant Account Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Miscellaneous",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Note Payable",
                "DebitAmount": -22739.32,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Office expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Opening Balance Equity",
                "DebitAmount": -3668.2,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Other Portfolio Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Contributions",
                "DebitAmount": -12750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Draws",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Penalties and settlements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Prepaid expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printed Materials purchased for clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printing and Reproduction",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Professional Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Promotional",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Purchases",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Refunds-Allowances",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent Expense",
                "DebitAmount": 6250.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent or lease payments",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Repair and maintenance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Retained Earnings",
                "DebitAmount": 2535.19,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales",
                "DebitAmount": -12250.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales Discounts",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales of Product Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Stationery and printing",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Subcontracted Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Supplies",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes - Property",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes and Licenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Telephone Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel meals",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Bill Payment Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Payment Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Undeposited Funds",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Electric \u0026 Gas",
                "DebitAmount": 1099.36,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Water",
                "DebitAmount": 299.16,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Vehicles",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Venue Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Visa Credit Card",
                "DebitAmount": -3831.8,
                "CreditAmount": 0.0,
                "Quality": []
            }
            ],
            "CreatedTimestamp": "2017-07-21 10:44:21.544000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.544000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Version": "1",
            "Period": "2016-06",
            "RecordedTimestamp": "2017-07-21 10:44:20.468000",
            "CustomerTrialBalanceItem": [{
                "AccountName": "Accounts Payable",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Payable (A/P) - HKD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable",
                "DebitAmount": -454.83,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable (A/R) - USD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accumulated Depreciation",
                "DebitAmount": -233.31,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Advertising",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Ask My Accountant",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Bank charges",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expense Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expenses Income",
                "DebitAmount": -23033.25,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Business Licenses and Permits",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Charitable Contributions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Chequing",
                "DebitAmount": 38850.61,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commission Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions and fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions Paid",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Computer and Internet Expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Continuing Education",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Goods Sold",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Sales - billable expenses",
                "DebitAmount": 16597.24,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Depreciation Expense",
                "DebitAmount": 233.31,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Discounts given",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Dues and Subscriptions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Entertainment Booking Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Equipment rental",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Exchange Gain or Loss",
                "DebitAmount": 18.36,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Fees Billed",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Furniture and Equipment",
                "DebitAmount": 2750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Payable",
                "DebitAmount": -1013.28,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Suspense",
                "DebitAmount": 1495.62,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-General Liability Insurance",
                "DebitAmount": 750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Health Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Life and Disability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest earned",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest expense",
                "DebitAmount": 665.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Asset",
                "DebitAmount": 8010.35,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Shrinkage",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Janitorial Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Leasehold Improvements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Legal and professional fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Markup",
                "DebitAmount": -1538.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Meals and entertainment",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Merchant Account Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Miscellaneous",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Note Payable",
                "DebitAmount": -22362.54,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Office expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Opening Balance Equity",
                "DebitAmount": -3668.2,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Other Portfolio Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Contributions",
                "DebitAmount": -12750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Draws",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Penalties and settlements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Prepaid expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printed Materials purchased for clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printing and Reproduction",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Professional Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Promotional",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Purchases",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Refunds-Allowances",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent Expense",
                "DebitAmount": 7500.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent or lease payments",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Repair and maintenance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Retained Earnings",
                "DebitAmount": 2535.19,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales",
                "DebitAmount": -12250.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales Discounts",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales of Product Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Stationery and printing",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Subcontracted Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Supplies",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes - Property",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes and Licenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Telephone Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel meals",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Bill Payment Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Payment Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Undeposited Funds",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Electric \u0026 Gas",
                "DebitAmount": 1348.58,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Water",
                "DebitAmount": 380.95,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Vehicles",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Venue Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Visa Credit Card",
                "DebitAmount": -3831.8,
                "CreditAmount": 0.0,
                "Quality": []
            }
            ],
            "CreatedTimestamp": "2017-07-21 10:44:21.544000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.544000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Version": "1",
            "Period": "2016-07",
            "RecordedTimestamp": "2017-07-21 10:44:20.468000",
            "CustomerTrialBalanceItem": [{
                "AccountName": "Accounts Payable",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Payable (A/P) - HKD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable",
                "DebitAmount": -454.83,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable (A/R) - USD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accumulated Depreciation",
                "DebitAmount": -266.64,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Advertising",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Ask My Accountant",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Bank charges",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expense Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expenses Income",
                "DebitAmount": -28524.75,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Business Licenses and Permits",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Charitable Contributions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Chequing",
                "DebitAmount": 46006.35,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commission Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions and fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions Paid",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Computer and Internet Expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Continuing Education",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Goods Sold",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Sales - billable expenses",
                "DebitAmount": 16597.24,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Depreciation Expense",
                "DebitAmount": 266.64,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Discounts given",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Dues and Subscriptions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Entertainment Booking Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Equipment rental",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Exchange Gain or Loss",
                "DebitAmount": 18.36,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Fees Billed",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Furniture and Equipment",
                "DebitAmount": 2750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Payable",
                "DebitAmount": -1890.79,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Suspense",
                "DebitAmount": 1495.62,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-General Liability Insurance",
                "DebitAmount": 1500.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Health Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Life and Disability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest earned",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest expense",
                "DebitAmount": 760.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Asset",
                "DebitAmount": 8010.35,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Shrinkage",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Janitorial Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Leasehold Improvements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Legal and professional fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Markup",
                "DebitAmount": -3096.3,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Meals and entertainment",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Merchant Account Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Miscellaneous",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Note Payable",
                "DebitAmount": -21985.76,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Office expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Opening Balance Equity",
                "DebitAmount": -3668.2,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Other Portfolio Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Contributions",
                "DebitAmount": -12750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Draws",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Penalties and settlements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Prepaid expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printed Materials purchased for clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printing and Reproduction",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Professional Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Promotional",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Purchases",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Refunds-Allowances",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent Expense",
                "DebitAmount": 8750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent or lease payments",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Repair and maintenance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Retained Earnings",
                "DebitAmount": 2535.19,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales",
                "DebitAmount": -14250.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales Discounts",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales of Product Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Stationery and printing",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Subcontracted Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Supplies",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes - Property",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes and Licenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Telephone Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel meals",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Bill Payment Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Payment Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Undeposited Funds",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Electric \u0026 Gas",
                "DebitAmount": 1573.41,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Water",
                "DebitAmount": 455.91,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Vehicles",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Venue Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Visa Credit Card",
                "DebitAmount": -3831.8,
                "CreditAmount": 0.0,
                "Quality": []
            }
            ],
            "CreatedTimestamp": "2017-07-21 10:44:21.544000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.544000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Version": "1",
            "Period": "2016-08",
            "RecordedTimestamp": "2017-07-21 10:44:20.468000",
            "CustomerTrialBalanceItem": [{
                "AccountName": "Accounts Payable",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Payable (A/P) - HKD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable",
                "DebitAmount": 7986.27,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable (A/R) - USD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accumulated Depreciation",
                "DebitAmount": -299.97,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Advertising",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Ask My Accountant",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Bank charges",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expense Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expenses Income",
                "DebitAmount": -33643.5,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Business Licenses and Permits",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Charitable Contributions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Chequing",
                "DebitAmount": 37022.62,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commission Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions and fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions Paid",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Computer and Internet Expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Continuing Education",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Goods Sold",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Sales - billable expenses",
                "DebitAmount": 21715.99,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Depreciation Expense",
                "DebitAmount": 299.97,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Discounts given",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Dues and Subscriptions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Entertainment Booking Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Equipment rental",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Exchange Gain or Loss",
                "DebitAmount": 18.36,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Fees Billed",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Furniture and Equipment",
                "DebitAmount": 2750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Payable",
                "DebitAmount": -1969.4,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Suspense",
                "DebitAmount": 1495.62,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-General Liability Insurance",
                "DebitAmount": 1500.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Health Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Life and Disability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest earned",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest expense",
                "DebitAmount": 855.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Asset",
                "DebitAmount": 8010.35,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Shrinkage",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Janitorial Expense",
                "DebitAmount": 217.52,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Leasehold Improvements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Legal and professional fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Markup",
                "DebitAmount": -3947.55,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Meals and entertainment",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Merchant Account Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Miscellaneous",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Note Payable",
                "DebitAmount": -21608.98,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Office expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Opening Balance Equity",
                "DebitAmount": -3668.2,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Other Portfolio Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Contributions",
                "DebitAmount": -12750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Draws",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Penalties and settlements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Prepaid expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printed Materials purchased for clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printing and Reproduction",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Professional Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Promotional",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Purchases",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Refunds-Allowances",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent Expense",
                "DebitAmount": 10000.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent or lease payments",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Repair and maintenance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Retained Earnings",
                "DebitAmount": 2535.19,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales",
                "DebitAmount": -15750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales Discounts",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales of Product Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Stationery and printing",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Subcontracted Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Supplies",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes - Property",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes and Licenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Telephone Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel meals",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Bill Payment Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Payment Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Undeposited Funds",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Electric \u0026 Gas",
                "DebitAmount": 1784.28,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Water",
                "DebitAmount": 524.03,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Vehicles",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Venue Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Visa Credit Card",
                "DebitAmount": -3077.6,
                "CreditAmount": 0.0,
                "Quality": []
            }
            ],
            "CreatedTimestamp": "2017-07-21 10:44:21.544000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.544000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Version": "1",
            "Period": "2016-09",
            "RecordedTimestamp": "2017-07-21 10:44:20.468000",
            "CustomerTrialBalanceItem": [{
                "AccountName": "Accounts Payable",
                "DebitAmount": -734.51,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Payable (A/P) - HKD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable",
                "DebitAmount": 6819.54,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable (A/R) - USD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accumulated Depreciation",
                "DebitAmount": -333.3,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Advertising",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Ask My Accountant",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Bank charges",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expense Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expenses Income",
                "DebitAmount": -33643.5,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Business Licenses and Permits",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Charitable Contributions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Chequing",
                "DebitAmount": 39883.86,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commission Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions and fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions Paid",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Computer and Internet Expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Continuing Education",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Goods Sold",
                "DebitAmount": 3301.74,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Sales - billable expenses",
                "DebitAmount": 24353.49,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Depreciation Expense",
                "DebitAmount": 333.3,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Discounts given",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Dues and Subscriptions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Entertainment Booking Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Equipment rental",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Exchange Gain or Loss",
                "DebitAmount": 18.36,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Fees Billed",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Furniture and Equipment",
                "DebitAmount": 2750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Payable",
                "DebitAmount": -2360.95,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Suspense",
                "DebitAmount": 1495.62,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-General Liability Insurance",
                "DebitAmount": 1500.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Health Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Life and Disability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest earned",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest expense",
                "DebitAmount": 1045.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Asset",
                "DebitAmount": 4708.61,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Shrinkage",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Janitorial Expense",
                "DebitAmount": 417.52,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Leasehold Improvements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Legal and professional fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Markup",
                "DebitAmount": -3947.55,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Meals and entertainment",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Merchant Account Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Miscellaneous",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Note Payable",
                "DebitAmount": -20855.42,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Office expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Opening Balance Equity",
                "DebitAmount": -3668.2,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Other Portfolio Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Contributions",
                "DebitAmount": -12750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Draws",
                "DebitAmount": 500.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Penalties and settlements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Prepaid expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printed Materials purchased for clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printing and Reproduction",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Professional Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Promotional",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Purchases",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Refunds-Allowances",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent Expense",
                "DebitAmount": 11250.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent or lease payments",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Repair and maintenance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Retained Earnings",
                "DebitAmount": 2535.19,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales",
                "DebitAmount": -15750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales Discounts",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales of Product Income",
                "DebitAmount": -6500.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Services",
                "DebitAmount": -800.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Stationery and printing",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Subcontracted Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Supplies",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes - Property",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes and Licenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Telephone Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel meals",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Bill Payment Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Payment Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Undeposited Funds",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Electric \u0026 Gas",
                "DebitAmount": 1984.77,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Water",
                "DebitAmount": 524.03,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Vehicles",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Venue Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Visa Credit Card",
                "DebitAmount": -2077.6,
                "CreditAmount": 0.0,
                "Quality": []
            }
            ],
            "CreatedTimestamp": "2017-07-21 10:44:21.544000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.544000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Version": "1",
            "Period": "2016-10",
            "RecordedTimestamp": "2017-07-21 10:44:20.468000",
            "CustomerTrialBalanceItem": [{
                "AccountName": "Accounts Payable",
                "DebitAmount": -734.51,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Payable (A/P) - HKD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable",
                "DebitAmount": 18402.04,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable (A/R) - USD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accumulated Depreciation",
                "DebitAmount": -366.63,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Advertising",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Ask My Accountant",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Bank charges",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expense Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expenses Income",
                "DebitAmount": -33643.5,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Business Licenses and Permits",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Charitable Contributions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Chequing",
                "DebitAmount": 18041.58,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commission Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions and fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions Paid",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Computer and Internet Expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Continuing Education",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Goods Sold",
                "DebitAmount": 7683.64,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Sales - billable expenses",
                "DebitAmount": 40103.49,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Depreciation Expense",
                "DebitAmount": 366.63,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Discounts given",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Dues and Subscriptions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Entertainment Booking Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Equipment rental",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Exchange Gain or Loss",
                "DebitAmount": 18.36,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Fees Billed",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Furniture and Equipment",
                "DebitAmount": 2750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Payable",
                "DebitAmount": -1349.94,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Suspense",
                "DebitAmount": 1495.62,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-General Liability Insurance",
                "DebitAmount": 2250.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Health Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Life and Disability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest earned",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest expense",
                "DebitAmount": 1140.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Asset",
                "DebitAmount": 9762.95,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Shrinkage",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Janitorial Expense",
                "DebitAmount": 417.52,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Leasehold Improvements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Legal and professional fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Markup",
                "DebitAmount": -3947.55,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Meals and entertainment",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Merchant Account Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Miscellaneous",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Note Payable",
                "DebitAmount": -20478.64,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Office expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Opening Balance Equity",
                "DebitAmount": -3668.2,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Other Portfolio Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Contributions",
                "DebitAmount": -12750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Draws",
                "DebitAmount": 1500.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Penalties and settlements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Prepaid expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printed Materials purchased for clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printing and Reproduction",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Professional Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Promotional",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Purchases",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Refunds-Allowances",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent Expense",
                "DebitAmount": 12500.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent or lease payments",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Repair and maintenance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Retained Earnings",
                "DebitAmount": -6901.05,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales",
                "DebitAmount": -15750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales Discounts",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales of Product Income",
                "DebitAmount": -15150.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Services",
                "DebitAmount": -2400.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Stationery and printing",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Subcontracted Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Supplies",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes - Property",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes and Licenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Telephone Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel meals",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Bill Payment Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Payment Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Undeposited Funds",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Electric \u0026 Gas",
                "DebitAmount": 2187.55,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Water",
                "DebitAmount": 598.24,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Vehicles",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Venue Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Visa Credit Card",
                "DebitAmount": -2077.6,
                "CreditAmount": 0.0,
                "Quality": []
            }
            ],
            "CreatedTimestamp": "2017-07-21 10:44:21.544000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.544000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Version": "1",
            "Period": "2016-11",
            "RecordedTimestamp": "2017-07-21 10:44:20.468000",
            "CustomerTrialBalanceItem": [{
                "AccountName": "Accounts Payable",
                "DebitAmount": -734.51,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Payable (A/P) - HKD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable",
                "DebitAmount": 18402.04,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable (A/R) - USD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accumulated Depreciation",
                "DebitAmount": -366.63,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Advertising",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Ask My Accountant",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Bank charges",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expense Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expenses Income",
                "DebitAmount": -33643.5,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Business Licenses and Permits",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Charitable Contributions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Chequing",
                "DebitAmount": 21095.57,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commission Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions and fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions Paid",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Computer and Internet Expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Continuing Education",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Goods Sold",
                "DebitAmount": 9664.68,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Sales - billable expenses",
                "DebitAmount": 40103.49,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Depreciation Expense",
                "DebitAmount": 366.63,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Discounts given",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Dues and Subscriptions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Entertainment Booking Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Equipment rental",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Exchange Gain or Loss",
                "DebitAmount": 18.36,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Fees Billed",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Furniture and Equipment",
                "DebitAmount": 2750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Payable",
                "DebitAmount": 23.23,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Suspense",
                "DebitAmount": -340.69,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-General Liability Insurance",
                "DebitAmount": 2250.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Health Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Life and Disability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest earned",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest expense",
                "DebitAmount": 1235.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Asset",
                "DebitAmount": 7781.91,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Shrinkage",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Janitorial Expense",
                "DebitAmount": 417.52,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Leasehold Improvements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Legal and professional fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Markup",
                "DebitAmount": -3947.55,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Meals and entertainment",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Merchant Account Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Miscellaneous",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Note Payable",
                "DebitAmount": -20101.86,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Office expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Opening Balance Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Other Portfolio Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Contributions",
                "DebitAmount": -12750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Draws",
                "DebitAmount": 2000.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Penalties and settlements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Prepaid expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printed Materials purchased for clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printing and Reproduction",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Professional Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Promotional",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Purchases",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Refunds-Allowances",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent Expense",
                "DebitAmount": 13750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent or lease payments",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Repair and maintenance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Retained Earnings",
                "DebitAmount": -10569.25,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales",
                "DebitAmount": -15750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales Discounts",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales of Product Income",
                "DebitAmount": -19050.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Services",
                "DebitAmount": -3600.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Stationery and printing",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Subcontracted Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Supplies",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes - Property",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes and Licenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Telephone Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel meals",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Bill Payment Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Payment Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Undeposited Funds",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Electric \u0026 Gas",
                "DebitAmount": 2403.07,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Water",
                "DebitAmount": 670.09,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Vehicles",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Venue Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Visa Credit Card",
                "DebitAmount": -2077.6,
                "CreditAmount": 0.0,
                "Quality": []
            }
            ],
            "CreatedTimestamp": "2017-07-21 10:44:21.544000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.544000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Version": "1",
            "Period": "2016-12",
            "RecordedTimestamp": "2017-07-21 10:44:20.468000",
            "CustomerTrialBalanceItem": [{
                "AccountName": "Accounts Payable",
                "DebitAmount": -734.51,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Payable (A/P) - HKD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable",
                "DebitAmount": 18402.04,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable (A/R) - USD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accumulated Depreciation",
                "DebitAmount": -366.63,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Advertising",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Ask My Accountant",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Bank charges",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expense Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expenses Income",
                "DebitAmount": -33643.5,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Business Licenses and Permits",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Charitable Contributions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Chequing",
                "DebitAmount": 21095.57,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commission Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions and fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions Paid",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Computer and Internet Expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Continuing Education",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Goods Sold",
                "DebitAmount": 9664.68,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Sales - billable expenses",
                "DebitAmount": 40103.49,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Depreciation Expense",
                "DebitAmount": 366.63,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Discounts given",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Dues and Subscriptions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Entertainment Booking Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Equipment rental",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Exchange Gain or Loss",
                "DebitAmount": 18.36,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Fees Billed",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Furniture and Equipment",
                "DebitAmount": 2750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Payable",
                "DebitAmount": 23.23,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Suspense",
                "DebitAmount": -340.69,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-General Liability Insurance",
                "DebitAmount": 2250.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Health Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Life and Disability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest earned",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest expense",
                "DebitAmount": 1235.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Asset",
                "DebitAmount": 7781.91,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Shrinkage",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Janitorial Expense",
                "DebitAmount": 417.52,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Leasehold Improvements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Legal and professional fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Markup",
                "DebitAmount": -3947.55,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Meals and entertainment",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Merchant Account Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Miscellaneous",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Note Payable",
                "DebitAmount": -20101.86,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Office expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Opening Balance Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Other Portfolio Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Contributions",
                "DebitAmount": -12750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Draws",
                "DebitAmount": 2000.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Penalties and settlements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Prepaid expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printed Materials purchased for clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printing and Reproduction",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Professional Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Promotional",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Purchases",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Refunds-Allowances",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent Expense",
                "DebitAmount": 13750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent or lease payments",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Repair and maintenance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Retained Earnings",
                "DebitAmount": -10569.25,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales",
                "DebitAmount": -15750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales Discounts",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales of Product Income",
                "DebitAmount": -19050.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Services",
                "DebitAmount": -3600.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Stationery and printing",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Subcontracted Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Supplies",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes - Property",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes and Licenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Telephone Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel meals",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Bill Payment Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Payment Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Undeposited Funds",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Electric \u0026 Gas",
                "DebitAmount": 2403.07,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Water",
                "DebitAmount": 670.09,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Vehicles",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Venue Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Visa Credit Card",
                "DebitAmount": -2077.6,
                "CreditAmount": 0.0,
                "Quality": []
            }
            ],
            "CreatedTimestamp": "2017-07-21 10:44:21.544000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.544000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }, {
            "Version": "1",
            "Period": "2017-01",
            "RecordedTimestamp": "2017-07-21 10:44:20.468000",
            "CustomerTrialBalanceItem": [{
                "AccountName": "Accounts Payable",
                "DebitAmount": -734.51,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Payable (A/P) - HKD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable",
                "DebitAmount": 18402.04,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accounts Receivable (A/R) - USD",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Accumulated Depreciation",
                "DebitAmount": -366.63,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Advertising",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Ask My Accountant",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Bank charges",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expense Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Billable Expenses Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Business Licenses and Permits",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Charitable Contributions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Chequing",
                "DebitAmount": 21095.57,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commission Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions and fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Commissions Paid",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Computer and Internet Expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Continuing Education",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Goods Sold",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Cost of Sales - billable expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Depreciation Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Discounts given",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Dues and Subscriptions",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Entertainment Booking Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Equipment rental",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Exchange Gain or Loss",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Fees Billed",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Furniture and Equipment",
                "DebitAmount": 2750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Payable",
                "DebitAmount": 23.23,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "GST/HST Suspense",
                "DebitAmount": -340.69,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-General Liability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Health Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Insurance Expense-Life and Disability Insurance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest earned",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Interest expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Asset",
                "DebitAmount": 7781.91,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Inventory Shrinkage",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Janitorial Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Leasehold Improvements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Legal and professional fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Markup",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Meals and entertainment",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Merchant Account Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Miscellaneous",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Note Payable",
                "DebitAmount": -20101.86,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Office expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Opening Balance Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Other Portfolio Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Contributions",
                "DebitAmount": -12750.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Owner\u0027s Equity - Draws",
                "DebitAmount": 2000.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Penalties and settlements",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Prepaid expenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printed Materials purchased for clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Printing and Reproduction",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Professional Fees",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Promotional",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Purchases",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Refunds-Allowances",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Rent or lease payments",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Repair and maintenance",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Retained Earnings",
                "DebitAmount": -15681.46,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales Discounts",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Sales of Product Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Stationery and printing",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Subcontracted Services",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Supplies",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes - Property",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Taxes and Licenses",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Telephone Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Travel meals",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Bill Payment Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Unapplied Cash Payment Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorised Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Asset",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Expense",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Uncategorized Income",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Undeposited Funds",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Electric \u0026 Gas",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Utilities - Water",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Vehicles",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Venue Fees paid on behalf of clients",
                "DebitAmount": 0.0,
                "CreditAmount": 0.0,
                "Quality": []
            }, {
                "AccountName": "Visa Credit Card",
                "DebitAmount": -2077.6,
                "CreditAmount": 0.0,
                "Quality": []
            }
            ],
            "CreatedTimestamp": "2017-07-21 10:44:21.544000",
            "LastUpdatedTimestamp": "2017-07-21 10:44:21.544000",
            "Quality": [],
            "SourceName": "WebApp",
            "SourceKey": "fai_test_01"
        }
        ],}
        return Response(data)


class CompanyLoginView(views.APIView):
    pass
