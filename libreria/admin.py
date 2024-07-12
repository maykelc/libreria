from django.contrib import admin
from libreria import models

# from .models import autor, libros, categoria, nav
# Register your models here.

# MODELOS DESDE MODELS
admin.site.register(models.autor)
admin.site.register(models.libros)
admin.site.register(models.Categoria)
admin.site.register(models.nav)
