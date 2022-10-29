from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

class Genero(models.Model):
    tipo = models.CharField(max_length=25)

    def __str__(self):
        return self.tipo

class Estado(models.Model):
    tipo = models.CharField(max_length=25)

    def __str__(self):
        return self.tipo



class Documento(models.Model):
    tipo = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.tipo

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Barrio(models.Model):
    nombre = models.CharField(max_length=50)
    Ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre



class Postulante(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=25)  
    apellido = models.CharField(max_length=25)  
    tipodocumento = models.ForeignKey(Documento,on_delete=models.CASCADE, max_length=50, blank=True, null=True, verbose_name = 'Tipo de Documento')
    numdocumento = models.CharField(max_length=25, blank=True, null=True, verbose_name = 'Numero de Documento')
    fechanacimiento = models.DateField(blank=True, null=True, verbose_name = 'Fecha de Nacimiento')
    direccion = models.CharField(max_length=100, blank=True, null=True)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, max_length=50, blank=True, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, max_length=50, blank=True, null=True)

    def __str__(self):
        fila = self.nombre + ' ' + self.apellido
        return fila
    

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class PostulanteTecnologia(models.Model):
    postulante = models.ForeignKey(Postulante, on_delete=models.CASCADE, max_length=50, blank=True, null=True)
    tecnologia = models.ForeignKey(Tecnologia, on_delete=models.CASCADE, max_length=50, blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)

    
 
class Idioma(models.Model):
    nombre = nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class PostulanteIdioma(models.Model):
    postulante = models.ForeignKey(Postulante, on_delete=models.CASCADE, max_length=50, blank=True, null=True, verbose_name ="ID Postulante")
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, max_length=50, blank=True, null=True, verbose_name ="ID idioma")
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, max_length=50, blank=True, null=True, verbose_name ="ID estado")
    descripcion = models.CharField(max_length=250, blank=True, null=True, verbose_name ="Descripcion")

    
# Modelado de la clase Organizaciones
class TipoOrganizacion(models.Model):
    tipo = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.tipo

class Organizacion(models.Model):
    razonsocial = models.CharField(max_length=250, blank=False, null=False, verbose_name='Razon Social')
    cuit = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    tipoorganizacion = models.ForeignKey(TipoOrganizacion,on_delete=models.CASCADE, max_length=50, blank=True, null=True, verbose_name='Tipo de Organizacion')
    
    def __str__(self):
        return self.razonsocial

class BusquedaLaboral(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, max_length=50, blank=True, null=True, verbose_name ="Id Organizacion")
    fechaApertura = models.DateField(blank=True, null=True)
    fechaCierre = models.DateField(blank=True, null=True)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, max_length=50, blank=True, null=True, verbose_name ="ID idioma")
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tecnologia = models.ManyToManyField(Tecnologia)











# Create your models here.
