from django.db import models

class SignalTest(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,primary_key=True,default="")

    def __str__(self) -> str:
        return self.name

