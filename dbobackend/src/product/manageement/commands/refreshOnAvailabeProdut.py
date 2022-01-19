from django.core.management.base import BaseCommand, CommandError
from product.models import Product
from product.serializers import ProductSerialisers
from product.config import baseUrl
import requests
import time


class Command(BaseCommand):
    help = 'Refresh the list of products which are on available product.'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        Product.objects.all().delete()
        for product in jsondata:
            serializer = ProductSerialisers(data=jsondata)
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS(
                    '['+time.ctime()+'] Successfully added product id="%s"' % product['id']))
        self.stdout.write('['+time.ctime()+'] Data refresh terminated.')
