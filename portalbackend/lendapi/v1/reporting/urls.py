from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^company/(?P<pk>[0-9]+)/monthlyreport/$', views.MonthlyReportList.as_view(), name='report-list'),

    url(r'^company/(?P<pk>[0-9]+)/monthlyreport/(?P<report_identifier>(\d{4}-\d{2}|[0-9]+))/$',
        views.MonthlyReportDetail.as_view(), name='report-detail'),

    url(r'^company/(?P<pk>[0-9]+)/monthlyreport/(?P<report_identifier>(\d{4}-\d{2}|[0-9]+))/status/$',
        views.MonthlyReportStatusDetail.as_view(), name='report-status'),

    url(r'^company/(?P<pk>[0-9]+)/monthlyreport/(?P<report_identifier>(\d{4}-\d{2}|[0-9]+))/edit/$',
        views.PreviousMonthlyReportEditDetails.as_view(), name='prev-report-edit'),

    # todo: this url needs to be deprecated because it is no longer neccessary to provide the period. The period is
    #       retrieved from the company metadata. Need to check through the UI code to see where it's used, and update.
    #       This can be done later because it won't cause any problems to call it like this, this date is just ignored.
    url(r'^company/(?P<pk>[0-9]+)/monthlyreport/signoff/$',
        views.MonthlyReportSignoff.as_view(), name='report-signoff'),

    url(r'^company/(?P<pk>[0-9]+)/monthlyreport/(?P<report_identifier>(\d{4}-\d{2}|[0-9]+))/questionnaire/$',
        views.QuestionnaireDetail.as_view(), name='report-questionnaire-details'),

    url(r'^company/(?P<pk>[0-9]+)/questionnaire/$',
        views.QuestionnaireList.as_view(), name='report-questionnaire-list'),
]
urlpatterns = format_suffix_patterns(urlpatterns)