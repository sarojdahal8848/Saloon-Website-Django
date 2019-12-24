from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def blog(request):
    blog_list = Blog.objects.filter(published=True).order_by('-id')
    recent_post = Blog.objects.filter(published=True).order_by('-id')[:6]
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context ={
        'blogs':blogs,
        'recent_posts' : recent_post
    }
    return render(request,'user/blog.html',context)


def blog_detail(request,id):
    
    # id = request.GET.get('id')
    blog = Blog.objects.get(id=id)
    recent_post = Blog.objects.filter(published=True).order_by('-id')[:6]
    context={
        'blogs':blog,
        'recent_posts':recent_post
    }
    return render(request,'user/blog_detail.html',context)
