from django.contrib import admin
from .models import Proyecto


class ProyectoAdmin(admin.ModelAdmin):
    readonly_fields = ["created","updated"]
# Register your models here.
admin.site.register(Proyecto,ProyectoAdmin)