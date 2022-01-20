from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.


class Sale(models.Model):
    category = models.IntegerField(default='-1')
    price = models.DecimalField(decimal_places=2, max_digits=1000, default='0')
    owner = models.TextField(max_length=100, default='')
    name = models.TextField(max_length=100, default='')
    quantity_sold = models.IntegerField(default='0')
    date = models.DateField(default=str(datetime.now())[0:10])

    class Meta:
        ordering = ('date',)
