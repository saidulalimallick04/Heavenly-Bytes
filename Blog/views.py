from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.

@login_required(login_url='/login/')
def blogHomePage(request):
    return render(request,"blog/blog_home_page.html")

@login_required(login_url='/login/')
def explorePage(request):
    
    return render(request,"blog/blog_explore_page.html")