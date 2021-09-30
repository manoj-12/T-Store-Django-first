
from django.contrib import admin
from django.urls import path
from .views import index , signup ,log_In
urlpatterns = [
  path('',index , name="indexpage"),
  path('signup' ,signup),
  path('login' ,log_In)
]
