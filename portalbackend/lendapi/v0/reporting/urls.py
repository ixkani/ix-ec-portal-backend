from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^company/(?P<pk>[0-9]+)/monthlyreport/$', views.MonthlyReportList.as_view(), name='report-list'),
    url(r'^company/(?P<pk>[0-9]+)/monthlyreport/(?P<period>\d{4}-\d{2})/$',
        views.MonthlyReportDetail.as_view(), name='report-detail'),
    url(r'^company/(?P<pk>[0-9]+)/monthlyreport/(?P<period>\d{4}-\d{2})/status/$',
        views.MonthlyReportStatusDetail.as_view(), name='report-status'),
    url(r'^company/(?P<pk>[0-9]+)/monthlyreport/(?P<period>\d{4}-\d{2})/signoff/$',
        views.MonthlyReportSignoff.as_view(), name='report-signoff'),
    url(r'^company/(?P<pk>[0-9]+)/monthlyreport/(?P<period>\d{4}-\d{2})/questionnaire/$',
        views.QuestionnaireList.as_view(), name='report-questionnaire'),
]
urlpatterns = format_suffix_patterns(urlpatterns)