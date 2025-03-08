from django.shortcuts import render

# Create your views here.


def inventoryOverview(request):
    
    return render(request, "inventory/inventory_overview_page.html")