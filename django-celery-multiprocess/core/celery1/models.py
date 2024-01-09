from django.db import models


class Mails(models.Model):
    email=models.CharField(max_length=100,null=True,blank=True)
    body=models.TextField(default="")
    subject=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self) -> str:
        return self.email
