from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from .forms import BusquedaLaboralForm ,PostulanteCrearForm, PostulanteSearchForm, IdiomaForm, OrganizacionForm, OrganizacionSearchForm

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def postulantes(request):
    header = "Listado de Postulantes"
    form = PostulanteSearchForm(request.POST or None)
    postulantes = Postulante.objects.all()
    context = {
        "header": header,
        "form": form,
        "postulantes": postulantes
    }
    if request.method == 'POST':
        postulantes = Postulante.objects.filter(nombre__icontains=form['nombre'].value(),
                                        apellido__icontains=form['apellido'].value()
                                        )
        context = {
        "header": header,
        "form": form,
        "postulantes": postulantes
    }
        
    return render(request, 'postulantes/index.html', context)

def crear(request):
    formulario = PostulanteCrearForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('postulantes')
    return render(request, 'postulantes/crear.html', {'formulario': formulario})

def editar(request, id):
    postulante = Postulante.objects.get(id=id)
    formulario = PostulanteCrearForm(request.POST or None, request.FILES or None, instance=postulante)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('postulantes')
    return render(request, 'postulantes/editar.html', {'formulario': formulario})

def eliminar(request, id):
    postulante = Postulante.objects.get(id=id)
    postulante.delete()
    return redirect('postulantes')

def idioma(request, id):
    postulante = Postulante.objects.get(id=id)
    formulario = IdiomaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid() :
        formulario.save()
        return redirect ('postulantes')
    return render(request, 'postulantes/idioma.html', {'formulario': formulario})

def crearOrganizacion(request):
    formulario = OrganizacionForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('organizaciones')
    return render(request, 'organizaciones/crear.html', {'formulario': formulario})

def organizaciones(request):
    header = "Listado de Organizaciones"
    form = OrganizacionSearchForm(request.POST or None)
    organizaciones = Organizacion.objects.all()
    context = {
        "header": header,
        "form": form,
        "organizaciones": organizaciones
    }
    if request.method == 'POST':
        organizaciones = Organizacion.objects.filter(razonsocial__icontains=form['razonsocial'].value())
        context = {
        "header": header,
        "form": form,
        "organizaciones": organizaciones
    }
        
    return render(request, 'organizaciones/index.html', context)

def editarOrganizacion(request, id):
    organizacion = Organizacion.objects.get(id=id)
    formulario = OrganizacionForm(request.POST or None, request.FILES or None, instance=organizacion)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('organizaciones')
    return render(request, 'organizaciones/editar.html', {'formulario': formulario})

def eliminarOrganizacion(request, id):
    organizacion = Organizacion.objects.get(id=id)
    organizacion.delete()
    return redirect('organizaciones')

def busquedaLaboral(request, id):
    
    
    organizacion = Organizacion.objects.get(id=id)
    formulario = BusquedaLaboralForm(request.POST or None, request.FILES or None)
    if formulario.is_valid() :
        formulario.save()
        return redirect ('organizaciones')
    return render(request, 'organizaciones/busquedaLaboral.html', {'formulario': formulario})

# Create your views here.
