from django.shortcuts import render
from .models import Category,Service



def service(request):
    service = Service.objects.filter(is_active=True)
    context ={
        'services':service
    }
    return render(request,'user/service.html',context)
