from django.contrib import admin
from django.urls import path
from . import views
from .views import proyectosList,detailProject

urlpatterns = [

    path('', proyectosList.as_view(), name = "proyectos"),
    path('detail/<int:pk>',detailProject.as_view(),name='detail')
    
    
    
]
