import django_filters
from portalbackend.lendapi.accounts.models import Company


class CompanyFilter(django_filters.FilterSet):
    """
    http://django-filter.readthedocs.io/en/develop/guide/rest_framework.html
    """
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Company
        fields = ['name', ]
