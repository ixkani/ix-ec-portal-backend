from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(title="API V1", renderer_classes=[SwaggerUIRenderer, OpenAPIRenderer],
                              urlconf='portalbackend.lendapi.v1.urls', description="V1 Api Documentation",
                              url="/lend/v1/")

urlpatterns = [
    url(r'^', include('portalbackend.lendapi.v1.accounts.urls'), name='accounts'),
    url(r'^', include('portalbackend.lendapi.v1.accounting.urls'), name='accounting'),
    url(r'^', include('portalbackend.lendapi.v1.reporting.urls'), name='reporting'),
    url(r'^docs/', schema_view)
]