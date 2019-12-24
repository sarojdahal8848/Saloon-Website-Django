from django.shortcuts import render
from .models import Saying,Contact,Team,Gallery,Review


def home(request):
    saying = Saying.objects.all()
    team = Team.objects.filter(is_active=True)[:3]
    review = Review.objects.all().order_by('-id')[:3]
    gallery = Gallery.objects.all().order_by('-id')[:4]
    context ={
        'sayings':saying,
        'teams':team,
        'reviews':review,
        'gallerys':gallery
    }
    return render(request,'user/home.html',context)


def contact(request):
    if request.method == 'POST':
        fullname = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        Contact.objects.create(fullname=fullname,message=message,email=email,subject=subject)
        context ={
            'sucess': 'Message has been successfully sent'
        }
        return render(request,'user/contact.html',context)
    else:
        return render(request,'user/contact.html')


def about(request):
    team = Team.objects.filter(is_active=True)
    context={
        'teams':team
    }
    return render(request,'user/about.html',context)


def gallery(request):
    gallery = Gallery.objects.filter(is_active=True)
    context={
        'gallerys':gallery
    }
    return render(request,'user/gallery.html',context)













