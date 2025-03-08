from django.shortcuts import render,redirect


# Create your views here.


def homePage(request):
    
    
    return render(request, "home/index.html")


def explorePage(request):
    
    
    return render(request, "home/explore_page.html")


def aboutUsPage(request):
    
    
    return render(request, 'home/about_us_page.html')


def contactUsPage(request):
    
    return render(request,"home/contact_us_page.html")