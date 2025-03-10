from django.db import models


from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class Order(models.Model):
    
    order_detail=models.ForeignKey("OrderDetail", on_delete=models.CASCADE)
    menu_category=models.ForeignKey("Menus.MenuCategory", on_delete=models.SET_DEFAULT, default="CategoryNotListed")
    menu_item=models.ForeignKey("Menus.MenuItem", on_delete=models.SET_DEFAULT, default="ItemNotListed")
    
    item_add_date=models.DateField( auto_now_add=True)
    status=models.CharField(max_length=20,default='Pending')
    count=models.IntegerField(default=1)
    
    total_amount=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    
    
    
class OrderDetail(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.SET_DEFAULT, default="UserDeleted")
    customer_email=models.CharField(max_length=25)
    
    order_date=models.DateField( auto_now_add=True)
    status=models.CharField(max_length=20,default='Placed')
    
    item_list_order_id=ArrayField(models.IntegerField())
    
    total_amount=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item_list_item_id=ArrayField(models.IntegerField())
    
    
    
    