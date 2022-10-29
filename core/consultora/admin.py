from django.contrib import admin
from .models import BusquedaLaboral, Organizacion, TipoOrganizacion, Postulante, Documento, Pais, Provincia, Genero, Ciudad, Barrio, Tecnologia, Idioma, PostulanteIdioma, PostulanteTecnologia, Estado
from .forms import PostulanteCrearForm, OrganizacionForm

class PostulanteCreateAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'tipodocumento', 'numdocumento', 'fechanacimiento']
    form = PostulanteCrearForm
    list_filter = ['apellido']
    search_fields = ['apellido', 'numdocumento']

class OrganizacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'razonsocial', 'cuit', 'tipoorganizacion']
    form = OrganizacionForm
    list_filter = ['razonsocial']
    search_fields = ['razonsocial']

admin.site.register(Postulante, PostulanteCreateAdmin)
admin.site.register(Documento)
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Barrio)
admin.site.register(Tecnologia)
admin.site.register(Idioma)
admin.site.register(PostulanteTecnologia)
admin.site.register(PostulanteIdioma)
admin.site.register(Estado)
admin.site.register(Genero)
admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(TipoOrganizacion)
admin.site.register(BusquedaLaboral)



# Register your models here.
