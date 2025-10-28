from icecream import ic
from rest_framework import serializers
from decimal import Decimal
from .models import Product, Collection,Review

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title','products_count']

    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','title','description','slug','unit_price','collection','inventory','price_with_tax']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')


    def calculate_tax(self,product:Product):
        return product.unit_price * Decimal(1.20)
    

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','date','name','description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        ic(product_id)
        ic(self.context)
        ic(validated_data)
        return Review.objects.create(product_id=product_id,**validated_data)
        
        # product_id : 1
        # self.context : {'product_id':1}
        # validated_data: {'description':'1.product icin 3.yorum','name':'erfan'}
