from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path("",menuOverview,name='Heavenly Bytes-Menus'),
    
    path("allproducts/<category_id>",seeAllProducts, name="Category Name"),
    path("productname/<item_id>",productOverview, name="Product Name")
]
