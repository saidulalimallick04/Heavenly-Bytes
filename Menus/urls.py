from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path("",menuOverview,name='Heavenly Bytes-Menus'),
    path("productname",productOverview, name="Product Name"),
    path("allproducts",seeAllProducts, name="Category Name")
    
]
