from django.db import models

class Persons(models.Model):
    id=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return self.name
