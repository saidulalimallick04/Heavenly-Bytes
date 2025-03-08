from django.shortcuts import render

# Create your views here.

def orderPage(request):
    
    return render(request, "orders/order_page.html")