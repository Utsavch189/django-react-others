from .models import User,Brand,Product,Test
from rest_framework import serializers
from django.db import transaction

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['product_id','product_name','created_at']
    
    def create(self, validated_data):
        print(validated_data)

class BrandSerializer(serializers.ModelSerializer):
    product=ProductSerializer(many=True)
    class Meta:
        model=Brand
        fields=['brand_id','owner','brand_name','created_at','product']
    
    @transaction.atomic() #-----> if any of db operation fails under create() everything should be rolled back
    def create(self, validated_data):

        """
        inputed json like : 

        {
            "brand_id": "brand4469877",
            "owner": "uts123",
            "brand_name": "Babylon",
            "created_at": "2023-12-22T13:10:20Z",
            "product": [
                {
                    "product_id": "productbabylon88",
                    "product_name": "Afgani Chicken",
                    "created_at": "2023-12-22T13:10:20Z"
                },
                ...{more}
            ]
        }

        In the owner field of Brand you need to put just owners pk.
        """

        product_data=validated_data.pop('product')
        brand=Brand.objects.create(brand_id=validated_data.get('brand_id'),owner=validated_data.get('owner'),brand_name=validated_data.get('brand_name'),created_at=validated_data.get('created_at'))
        for data in product_data:
           Product.objects.create(product_id=data.get('product_id'),brand=brand,product_name=data.get('product_name'),created_at=data.get('created_at'))
        return brand



class UserSerializer(serializers.ModelSerializer):
    brand=BrandSerializer(many=True)
    class Meta:
        model=User
        fields=['user_id','name','email','brand']
    
    def create(self, validated_data):
        print(validated_data)

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Test
        fields='__all__'
    
    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)