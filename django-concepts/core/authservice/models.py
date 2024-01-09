from django.db import models

class MyUser(models.Model):
    username=models.CharField(max_length=50,primary_key=True,default="")
    password=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.username
    
class UserDetails(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()

    def __str__(self) -> str:
        return str(self.user)
