from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    
    path("",blogHomePage,name='Heavenly Blogs'),
    path("exploreblog/",explorePage,name='Heavenly Bytes-Explore'),
    
    
]
