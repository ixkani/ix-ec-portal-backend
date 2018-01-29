"""portalbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404,handler500

handler404 = 'portalbackend.validator.validator.custom404'
handler500 = 'portalbackend.validator.validator.custom500'
urlpatterns = [
    # allows staff login,
    url(r'^login', views.login, {'template_name': 'login.html'}, name='login'),

    # all admin views
    url(r'^admin/', admin.site.urls),

    # oauth views
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # our api's views
    url(r'^lend/', include('portalbackend.lendapi.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

