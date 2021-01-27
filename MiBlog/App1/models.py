from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=200,verbose_name="Nombre")
    content  = models.TextField(verbose_name = "Contenido")
    image = models.ImageField(verbose_name= "Imagen", upload_to = "Blog")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now = True, verbose_name="Editado")
    
    class Meta():
        verbose_name = "Blog"
        verbose_name_plural= "Blogs"
        ordering = ["-created"]
    def __str__(self):
        return self.name