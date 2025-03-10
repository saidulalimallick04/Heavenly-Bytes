from django.db import models

# Create your models here.

class MenuCategory(models.Model):
    
    name=models.CharField(max_length=75,unique=True)
    descriptions=models.TextField(max_length=200)
    order_count=models.IntegerField(default=0)
    is_active=models.BooleanField(default=True)
    
    class Meta:
        ordering=['name']
        verbose_name="Menu Category"
        verbose_name_plural="Menu Categories"
    
    def __str__(self) -> str:
        return self.name
    
    
#-----------------------------------------------------------------------------------------------------------

class MenuItem(models.Model):
    
    MenuCategory=models.ForeignKey("MenuCategory", on_delete=models.CASCADE)
    name=models.CharField(max_length=75,unique=True)
    image=models.ImageField(upload_to=None,null=True,blank=True)
    descriptions=models.TextField(max_length=200)
    order_count=models.IntegerField(default=0)
    
    is_active=models.BooleanField(default=True)
    created_at=models.DateField(auto_now_add=True)
    
    price=models.DecimalField(max_digits=10, decimal_places=2)
    is_available=models.BooleanField(default=True)
    
    class Meta:
        ordering=['name']
        verbose_name="Menu Item"
        verbose_name_plural="Menu Items"
        
    def __str__(self):
        return self.name