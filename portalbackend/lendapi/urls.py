from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import utils

urlpatterns = [
    url(r'^$', utils.index, name='index'),
    url(r'v0/', include('portalbackend.lendapi.v0.urls'), name='v0'),
    url(r'v1/', include('portalbackend.lendapi.v1.urls'), name='v1'),
    url(r'documentation', utils.documentation, name='documentation'),
    url(r'downloadqbd', utils.download_qbd_app, name='downloadqbd')
]
