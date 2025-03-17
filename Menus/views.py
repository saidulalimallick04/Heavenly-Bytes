from django.shortcuts import render
from .models import *
from Orders.models import Cart
# Create your views here.

def menuOverview(request):
    
    MenuCategoryName=[]
    QUERYSET=[]
    
    for i in range(1,12):
        
        MenuCategoryName.append(MenuCategory.objects.get(id=i).name)
        SUBSET=MenuItem.objects.filter(MenuCategory_id=i).order_by('-order_count')[1:4]
        QUERYSET.append(SUBSET)
        
    
    tx=zip(QUERYSET,MenuCategoryName)
    context={
        
        "AllItems":tx
        
    }
    
    return render(request, "menus/menu_overview_page.html",context)

#--------------------------------------------------------------------------------------------------

def seeAllProducts(request, category_id):
    
    category_name=MenuCategory.objects.get(id=category_id).name
    
    QUERYSET= MenuItem.objects.filter(MenuCategory_id=category_id)
    
    context={
        "Category_Name":category_name,
        "Items": QUERYSET
        
    }
    return render (request, 'menus/see_all_products_page.html',context)

#--------------------------------------------------------------------------------------------------

def productOverview(request,item_id):
    
    if request.method=="POST":
        data=request.POST
        
        # item_id= data.get("item_id")
        Count=data.get('Count')
        
        already_contain=Cart.objects.filter(item_list__contain=[item_id])
        user_contain=Cart.objects.filter(id=request.user.id)
        
        
        if user_contain is None or already_contain is None:
            
            Cart.objects.create(user_id=request.user.id,item_list_item_id=[item_id])
            
        elif user_contain is not None  or already_contain is None:
            
            ux=Cart.objects.filter(id=request.user.id)
        
    QUERYITEM= MenuItem.objects.get(id=item_id)
    
    context={
        "item": QUERYITEM
        
    }
    
    return render(request, "menus/product_overview.html",context)
