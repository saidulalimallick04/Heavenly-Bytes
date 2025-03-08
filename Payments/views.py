from django.shortcuts import render

# Create your views here.


def paymentHomepage(request):
    
    return render(request, "payments/payment_home_page.html")