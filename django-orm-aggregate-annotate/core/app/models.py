from django.db import models

class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customers')
    quant=models.PositiveSmallIntegerField()
    amount=models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.customer.name
