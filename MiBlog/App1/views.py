from django.shortcuts import render
from .models import Blog
from django.views import generic
# Create your views here.

class aboutListView(generic.ListView):
    model = Blog
    template_name = 'App1/about.html'
