from django.db import models

class User(models.Model):
    userid=models.CharField(max_length=30,primary_key=True,default="")
    username=models.CharField(max_length=50,null=True,blank=True)

class Resturant(models.Model):
    rest_id=models.CharField(max_length=30,primary_key=True,default="")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='rest_user')
    restname=models.CharField(max_length=50,null=True,blank=True)


class Role(models.Model):
    role_id=models.CharField(max_length=10,primary_key=True,default="")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='role_user')
    resturant=models.ForeignKey(Resturant,on_delete=models.CASCADE,related_name='role_rest')
    role_name=models.CharField(max_length=50,null=True,blank=True)

