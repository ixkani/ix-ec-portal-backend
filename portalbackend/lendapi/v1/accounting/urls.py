from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^connect/?$', views.CreateConnection.as_view(), name='connect'),
    url(r'^qbo/authCodeHandler/?$', views.QuickBooksAuthCodeHandler.as_view(), name='qbo-authCodeHandler'),
    url(r'^xero/authCodeHandler/(?P<pk>[0-9]+)/$', views.XeroAuthCodeHandler.as_view(), name='xero-authCodeHandler'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/refresh/?$', views.RefreshToken.as_view(), name='refresh'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/disconnect/?$', views.DisconnectToken.as_view(), name='disconnect'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/trialbalance/?$', views.TrialBalanceView.as_view(), name='trial-balance'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/chartofaccounts/?$', views.ChartOfAccounts.as_view(),
        name='chart-of-accounts'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/isvalid/?$', views.TokenValid.as_view(), name='qbo-valid'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/loginstatus/?$', views.LoginStatus.as_view(),
        name='qbo-status'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/generatestatements/?$', views.Statement.as_view(), name='statement-view'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/balancesheet/?$', views.BalanceSheetView.as_view(), name='balance-sheet'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/incomestatement/?$', views.IncomeStatementView.as_view(),
        name='income-statement'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/coamap/?$', views.CoaMapView.as_view(), name='coa-map'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/generatepdf/?$', views.GeneratePDF.as_view(), name='generate-pdf'),
    # Espresso URLS

]