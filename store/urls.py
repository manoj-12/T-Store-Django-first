
from django.contrib import admin
from django.urls import path
from .views .index import  index
from .views .signup import signup
from .views .login import log_In , logout

urlpatterns = [
  path('',index , name="indexpage"),
  path('signup' ,signup),
  path('login' ,log_In , name='login' ),
  path('logout' , logout, name='logout')
]
