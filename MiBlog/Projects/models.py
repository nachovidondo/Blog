from django.db import models

from django.contrib.auth.models  import User
from django.db.models.deletion import CASCADE
# Create your models here.
class Proyecto(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo ")
    subtitle = models.CharField(max_length=200,verbose_name="Subtitulo")
    content = models.TextField(verbose_name = "Contenido")
    image = models.ImageField(verbose_name ="Imagen", upload_to = "Projects")
    created= models.DateTimeField(auto_now_add= True, verbose_name= "Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name ="Editado")
    
    class Meta():
        verbose_name ="Proyecto"
        verbose_name_plural= "Proyectos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title