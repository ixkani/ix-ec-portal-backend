from django.shortcuts import render, HttpResponse,redirect
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import os
from django.conf import settings
from django.http import HttpResponse
from portalbackend import settings
# noinspection PyUnusedLocal
def index(request):
    auth_cancel_url = settings.QBO_AUTH_CANCEL_URL
    return redirect(auth_cancel_url)


# Limits the request to return an unpaginated list of items
class PageNumberPaginationDataOnly(PageNumberPagination):
    page_size = 1000
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(data)


def rename_keys(d, nameset):
    for s in nameset:
        try:
            d[s[1]] = d.pop(s[0])
        except KeyError:
            pass
    return d


def parse_url_params(b):
    param_list = {}
    params = b.split('&')
    for pset in params:
        values = pset.split('=')
        if len(values) > 1:
            param_list[values[0]] = values[1]
    return param_list


def documentation(request):
    return render(request, 'documentation.html')


# todo: make this generic. Right now it only downloads the quickbooks desktop app, but for the forseable future
#       that is all it will ever need
def download_qbd_app(request):
    qbd_file_name = os.environ.get('QUICKBOOKS_DESKTOP_APP_FILE_NAME')

    if not qbd_file_name:
        qbd_file_name = 'EspressoMonitorInstaller.msi'

    file_path = os.path.join(settings.MEDIA_ROOT, qbd_file_name)
    if file_path:
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/exe")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)

    return response
