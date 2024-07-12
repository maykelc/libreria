from django.db import models

# Create your models here.

# MODELO DE AUTOR
class autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=70)
        
    def __str__(self):
            return self.nombre
        

# MODELO DE LIBROS
class libros(models.Model):
    titulo = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.titulo
    
    
# MODELO DE CATEGORIA
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    description_cat = models.TextField()
    
    def __str__(self):
         return self.nombre
    
    
# MODELO DE NAV
class nav(models.Model):
    titulo_nav = models.CharField(max_length=200)
    url_nav = models.CharField(max_length=200)
    
    def __str__(self):
         return self.titulo_nav
