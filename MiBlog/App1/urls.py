from django.contrib import admin
from django.urls import path
from .views import aboutListView

urlpatterns = [

    path('about/', aboutListView.as_view(), name = "about"),
    
    
    
]
