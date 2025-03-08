from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .manager import UserManager


class CustomUser(AbstractUser):
    
    phone_number=models.CharField(max_length=20,blank=True)
    email=models.EmailField(unique=True)
    is_verified=models.BooleanField(default=False)
    username=None
    about_me=models.TextField(max_length=20,blank=True,null=True)
    location=models.TextField(max_length=20,blank=True,null=True)
    profile_pic=models.ImageField(upload_to="ProfilePicture",null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    gender=models.TextField(max_length=50,null=True,blank=True)
    
    user_ott=models.TextField(max_length=7,null=True,blank=True)
    USERNAME_FIELD=('email')
    REQUIRED_FIELDS=[]
    
    def __str__(self):
        return self.email
    
    objects=UserManager()
    
    def __str__(self) -> str:
        return self.email