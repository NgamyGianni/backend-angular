from rest_framework.serializers import ModelSerializer
from product.models import Product


class ProductSerialisers(ModelSerializer):
    class Meta:
        model = Product
        fields = ('comments', 'category', 'availability', 'price', 'price_on_sale',
                  'discount', 'sale', 'owner', 'unit', 'name')
