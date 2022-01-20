from sale.models import Sale
from sale.serializers import SaleSerialisers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SaleDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Sale.objects.get(id=pk)
        except Sale.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sale = self.get_object(pk)
        serializer = SaleSerialisers(sale)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sale = self.get_object(pk)
        serializer = SaleSerialisers(sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SaleList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, format=None):
        sales = Sale.objects.all()
        serializer = SaleSerialisers(sales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SaleSerialisers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
