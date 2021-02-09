from django.shortcuts import get_object_or_404, render
from .models import Proyecto
from django.views import generic

# Create your views here.

class proyectosList(generic.ListView):
    model = Proyecto
    template_name= 'Proyecto/proyectos.html'
   
    
class detailProject(generic.DetailView):
    model=Proyecto
    template_name='Proyecto/detail.html'
    

