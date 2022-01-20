from sale.models import Sale
from sale.serializers import SaleSerialisers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Sale(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Sale.objects.get(id=pk)
        except Sale.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SaleSerialisers(snippet)
        return Response(serializer.data)

class SaleList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, format=None):
        result = []
        for prod in Sale.objects.all():
            serializer = SaleSerialisers(prod)
            res.append(Response(serializer.data))
        return JsonResponse(res, safe=False)