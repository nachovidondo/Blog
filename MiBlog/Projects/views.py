from django.shortcuts import get_object_or_404, render
from .models import Proyecto

# Create your views here.
def proyectos(request):
    proyectos= Proyecto.objects.all()
    return render (request,'Proyecto/proyectos.html',{'proyectos' : proyectos})

def detail(request,proyecto_id):
    details=get_object_or_404(Proyecto,pk = proyecto_id)
    
    return render(request,'Proyecto/detail.html',{'details':details})