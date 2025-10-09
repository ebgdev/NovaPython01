from rest_framework import serializers
from decimal import Decimal
from .models import Product, Collection

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','title','unit_price','collection','price_with_tax']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')


    def calculate_tax(self,product:Product):
        return product.unit_price * Decimal(1.20)
    