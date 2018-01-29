from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(title="API V0", renderer_classes=[SwaggerUIRenderer, OpenAPIRenderer],
                              urlconf='portalbackend.lendapi.v0.urls', description="V0 Api Documentation",
                              url='/lend/v0/')

urlpatterns = [
    url(r'^', include('portalbackend.lendapi.v0.accounts.urls'), name='v0.accounts'),
    url(r'^', include('portalbackend.lendapi.v0.reporting.urls'), name='v0.reporting'),
    url(r'^', include('portalbackend.lendapi.v0.accounting.urls'), name='v0.accounting'),
    url(r'^docs/', schema_view)
]
