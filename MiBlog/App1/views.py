from django.shortcuts import render
from .models import Blog
# Create your views here.


def about(request):
    blogs = Blog.objects.all()
    return render (request,'App1/about.html',{'blogs' : blogs })