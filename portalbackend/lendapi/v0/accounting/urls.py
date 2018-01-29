from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^company/(?P<pk>[0-9]+)/accounting/login/(?P<system_name>)/$', views.CompanyLoginView.as_view(),  name='accounting-login'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/balancesheet/$', views.BalanceSheetDetail.as_view(), name='balance-sheet'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/trialbalance/$', views.TrialBalanceDetail.as_view(), name='trial-balance'),
    url(r'^company/(?P<pk>[0-9]+)/accounting/incomestatement/$',
        views.IncomeStatementDetail.as_view(), name='income-statement'),

]
urlpatterns = format_suffix_patterns(urlpatterns)