from django.db import models
from .category import Cotegory

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    Price = models.IntegerField()
    category = models.ForeignKey(Cotegory, on_delete=models.CASCADE,default=1)
    Desc = models.CharField(max_length=50, default='',null=True,blank=True)
    img = models.ImageField(upload_to='product/')

