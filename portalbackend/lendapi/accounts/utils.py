from .models import Company
from django.http import Http404

class AccountsUtils(object):

    @staticmethod
    def get_company(pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

