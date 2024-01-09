from django.db import models
from datetime import datetime

class User(models.Model):
    user_id=models.CharField(max_length=100,primary_key=True,default="")
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    brand_id=models.CharField(max_length=100,primary_key=True,default="")
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='brand')
    brand_name=models.CharField(max_length=100,null=True,blank=True)
    created_at=models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.brand_name

class Product(models.Model):
    product_id=models.CharField(max_length=100,primary_key=True,default="")
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='product')
    product_name=models.CharField(max_length=100,null=True,blank=True)
    created_at=models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.product_name

class Test(models.Model):
    id=models.CharField(max_length=100,primary_key=True,default="")
    name=models.CharField(max_length=100,null=True,blank=True)