from django.shortcuts import render
from rate.models import Service
from .models import Book

def book(request):

    if request.method=='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        datetime = request.POST.get('datetime')
        service = request.POST.get('service')
        Book.objects.create(fname=fname,lname=lname,phone=phone,address=address,datetime=datetime,service=service)
        return render(request,'user/book.html',{'success':'Your Booking Has Been Successfully Registered'})
    else:
        book = Service.objects.filter(is_active=True)
        context ={
            'books':book
        }
        return render(request,'user/book.html',context)
