
from django.contrib import admin
from django.urls import path
from .views .index import  index
from .views .signup import signup
from .views .login import log_In , logout
from .views .cart import cart
from .views .checkout import checkout
from .views .order import order
urlpatterns = [
  path('',index , name="indexpage"),
  path('signup' ,signup),
  path('login' ,log_In , name='login' ),
  path('logout' , logout, name='logout'),
  path('cart' , cart, name='cart'),
  path('checkout' , checkout , name='checkout'),
  path('order' , order , name='order')
]
