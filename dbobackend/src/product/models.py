from django.db import models

# Create your models here.


class Product(models.Model):
    comments = models.TextField(max_length=100, blank=True)
    category = models.IntegerField(blank=True)
    availability = models.BooleanField()
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    price_on_sale = models.DecimalField(max_digits=1000, decimal_places=2,)
    discount = models.DecimalField
    sale = models.BooleanField()
    owner = models.TextField(max_length=100)
    unit = models.TextField(max_length=10)
    name = models.TextField(max_length=100)
    quantity_stock = models.IntegerField()
    quantity_sold = models.IntegerField()
