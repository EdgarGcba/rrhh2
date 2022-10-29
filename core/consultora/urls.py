from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    
    path('postulantes', views.postulantes, name='postulantes'),
    path('postulantes/crear', views.crear, name='crear'),
    path('postulantes/editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('postulantes/idioma/<int:id>', views.idioma, name='idioma'),
    path('organizaciones', views.organizaciones, name='organizaciones'),
    path('organizaciones/crear', views.crearOrganizacion, name='crearOrganizacion'),
    path('organizaciones/editar/<int:id>', views.editarOrganizacion, name='editarOrganizacion'),
    path('eliminarOrganizacion/<int:id>', views.eliminarOrganizacion, name='eliminarOrganizacion'),
    path('organizaciones/busquedaLaboral/<int:id>', views.busquedaLaboral, name='busquedaLaboral'),
    

]