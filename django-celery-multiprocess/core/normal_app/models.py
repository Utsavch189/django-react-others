from django.db import models

class OTP(models.Model):
    email=models.CharField(max_length=30,null=True,blank=True)
    otp=models.IntegerField()
    expires=models.CharField(max_length=10,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.otp)