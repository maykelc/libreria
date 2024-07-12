from django.urls import path # IMPORTO PATH PARA USAR URLPATTERNS
from libreria import views
## MANIPULA LAS URLS PARA QUE SE VEA MAS LIGERO DE URLS.PY DE MISITIO
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cat_autor/',views.cat_autores, name='cat_autor'),
    path('cat_lib/',views.cat_libros, name='cat_lib'),
    path('categorias/',views.categoria, name='categorias')
]