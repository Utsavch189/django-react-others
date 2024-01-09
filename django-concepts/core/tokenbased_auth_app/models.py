from django.contrib.auth.models import AbstractUser
from django.db import models

# My Custom User Model
class Customer(AbstractUser):
    phone=models.CharField(max_length=10,null=True,blank=True)

    class Meta:
        __name__='Customer'

    def __str__(self) -> str:
        return self.username
    
from django.contrib.auth.base_user import BaseUserManager

class Usermanager(BaseUserManager):
    def create_user(self,phone,password=None,**extra):
        user=self.model(phone=phone,**extra)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,phone,password=None,**extra):
        extra.setdefault('is_staff',True)
        extra.setdefault('is_superuser',True)
        extra.setdefault('is_active',True)
        return self.create_user(phone,password,**extra)