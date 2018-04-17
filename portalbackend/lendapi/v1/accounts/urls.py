from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^company/$', views.CompanyList.as_view(), name='company-list'),
    url(r'^company/(?P<pk>[0-9]+)/$', views.CompanyDetail.as_view(), name='company-detail'),
    url(r'^company/(?P<pk>[0-9]+)/companymeta/$', views.CompanyMetaDetail.as_view(), name='company-meta'),

    url(r'^company/(?P<pk>[0-9]+)/contacts/$', views.ContactDetails.as_view(),name='company-contacts-list'),
    url(r'^company/(?P<pk>[0-9]+)/contacts/(?P<cid>[0-9]+)/$', views.ContactDetails.as_view(),name='company-contacts-list'),
    url(r'^company/(?P<pk>[0-9]+)/espresso_contact/$', views.EspressoContacts.as_view(),name='company-special-contacts-list'),
    url(r'^company/(?P<pk>[0-9]+)/espresso_contact/(?P<cid>[0-9]+)/$', views.EspressoContacts.as_view(),name='company-special-contacts-list'),

    # url(r'^company/(?P<pk>[0-9]+)/espressocontact/$', views.EspressoContactDetail.as_view(),
    #    name='company-contacts'),

    url(r'^user/$', views.UserList.as_view(), name='user-list'),
    url(r'^change_password/token/validate/$', views.EmailValidation.as_view(), name='validate-forgot-password'),
    url(r'^change_password/(?P<token>[\w\-]+)/$', views.ForgotPassword.as_view(), name='forgot-password'),
    url(r'^change_password/$', views.ChangePassword.as_view(), name='change-password'),
    url(r'^scheduled_maintenance/$', views.ScheduledMaintenanceDetails.as_view(), name='scheduled-maintenance'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),

    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^twofactor/auth/$', views.TwoFactorAuthenticationDetails.as_view(), name='twofactor-auth'),
    url(r'^user/me/$', views.Me.as_view(), name='me')
]
urlpatterns = format_suffix_patterns(urlpatterns)
