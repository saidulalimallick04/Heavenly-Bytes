from django.shortcuts import render

# Create your views here.

def notificationsHomepage(request):
    
    return render(request, "notifications/notifications_home_page.html")