from django.contrib import admin
from .models.category import Cotegory
from .models.product import Product
from .models.customer import Customer
from .models.orders import Order

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name', 'Price', 'category']
    list_filter = ['Price' , 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['category']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone']

class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer','Quantity','Phone' ,'Address']

admin.site.register(Product, AdminProduct)
admin.site.register(Cotegory , AdminCategory )
admin.site.register(Customer , AdminCustomer)
admin.site.register(Order , AdminOrder)
