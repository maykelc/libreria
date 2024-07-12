from django.shortcuts import render
from .models import autor, libros, Categoria, nav
# from libreria import models
# Create your views here.


# VISTAS DE LAS PAGINAS 
def inicio(request):
    return render(request,'inicio.html')

def cat_autores(request):
    autores = autor.objects.all() # GUARDO EN LA VARIABLE AUTORES LO QUE HAY EN AUTOR.OBJECTS.ALL() DE LA BD 
    return render(request,'catautores.html', {'autores': autores}) # ACA LO PASO A LA PAGINA catautores.html  PARA USARLO EN EL HTML

def cat_libros(request):
    query = request.GET.get('q') # GUARDA LO QUE VIENE DE  q ( DONDE ESTAN LOS DATOS DE LIBRO, EN UN NOMBRE INTERNO, NO SE MANIPULA )
    if query: 
        libross = libros.objects.filter(titulo__icontains=query) # FILTRAMOS PARA OBTENER EL TITULO
    else:
        libross= libros.objects.all() # GUARDA LO QUE HAY EN LIBROSS
    return render(request,'catlibros.html', {'libross': libross}) # SE PASA A LA PAGINA catlibros.html A TRAVES DE {'libross': libross} 

def categoria(request):
    categorias = Categoria.objects.all()  # GUARDA EN LA VARIABLE LO QUE HAY EN CATEGORIA 
    return render(request,'categoria.html', {'categorias': categorias})