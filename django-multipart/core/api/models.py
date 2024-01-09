from django.db import models

class People(models.Model):

    def __nameFile(instance, filename):
        return '/'.join([ str(instance.username), filename])

    username=models.CharField(max_length=100,primary_key=True,default="")
    name=models.CharField(max_length=100,blank=True,null=True)
    pic=models.ImageField(upload_to=__nameFile,blank=True,null=True)

    def __str__(self) -> str:
        return self.name
