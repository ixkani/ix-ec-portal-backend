from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^company/$', views.CompanyList.as_view(), name='company-list'),
    url(r'^company/(?P<pk>[0-9]+)/$', views.CompanyDetail.as_view(), name='company-detail'),
    url(r'^company/(?P<pk>[0-9]+)/companymeta/$', views.CompanyMetaDetail.as_view(), name='company-meta'),
    url(r'^user/$', views.UserList.as_view(), name='user-list'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
]
urlpatterns = format_suffix_patterns(urlpatterns)