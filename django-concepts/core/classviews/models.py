from django.db import models

class MyBooks(models.Model):
    book_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    price=models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
    def discount_price(self,disc):
        return self.price-(((self.price)/100)*disc)