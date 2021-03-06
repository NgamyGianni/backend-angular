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
        purchase = self.get_object(pk)
        serializer = PurchaseSerialisers(purchase)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        purchase = self.get_object(pk)
        serializer = PurchaseSerialisers(purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, format=None):
        purchaseList = Purchase.objects.all()
        serializer = PurchaseSerialisers(purchaseList, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PurchaseSerialisers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
