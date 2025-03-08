from django.shortcuts import render

# Create your views here.

def menuOverview(request):
    
    return render(request, "menus/menu_overview_page.html")



def productOverview(request):
    
    return render(request, "menus/product_overview.html")


def seeAllProducts(request):
    
    return render (request, 'menus/see_all_products_page.html')