from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.IntegerField()
    Phone = models.CharField(max_length=50 , default="" , blank=True)
    Address = models.CharField(max_length=250 , default="" , blank=True)
    Date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

