from purchase.models import Purchase
from purchase.serializers import PurchaseSerialisers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PurchaseDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Purchase.objects.get(id=pk)
        except Purchase.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PurchaseSerialisers(snippet)
        return Response(serializer.data)

class PurchaseList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, format=None):
        result = []
        for prod in Purchase.objects.all():
            serializer = PurchaseSerialisers(prod)
            res.append(Response(serializer.data))
        return JsonResponse(res, safe=False)