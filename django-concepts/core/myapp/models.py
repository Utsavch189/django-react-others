from django.db import models

class Books(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    price=models.PositiveIntegerField(default=0,null=True,blank=True)

    def __str__(self) -> str:
        return self.name