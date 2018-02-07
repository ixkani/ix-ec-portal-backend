from portalbackend.lendapi.v1.accounting.utils import Utils
from portalbackend.lendapi.accounting.models import TrialBalance
from portalbackend.lendapi.v1.accounting.serializers import TrialBalanceSerializer


class SageAccountings(object):

    def trail_balance(self, id, request):
        """
        Get Trail Balance From Database
        :param id: Company Id
        :return: Response
        """
        try:
            entries = TrialBalance.objects.filter(company=id)
            serializer = TrialBalanceSerializer(entries, many=True)
            if len(serializer.data) > 0:
                return Utils.dispatch_success(request, serializer.data)
            return Utils.dispatch_success(request, 'NO_DATA_CHANGES')

        except Exception:
            return Utils.dispatch_failure(request, "INTERNAL_SERVER_ERROR")
