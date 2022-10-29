from django import forms
from .models import *

class PostulanteCrearForm(forms.ModelForm):   
    
    class Meta:
        model = Postulante
        fields = '__all__'
class PostulanteSearchForm(forms.ModelForm):
   class Meta:
     model = Postulante
     fields = ['nombre', 'apellido']

class IdiomaForm(forms.ModelForm):   

    class Meta:
        model = PostulanteIdioma
        fields = '__all__'

class OrganizacionSearchForm(forms.ModelForm):
   class Meta:
     model = Organizacion
     fields = ['razonsocial']

class OrganizacionForm(forms.ModelForm):   
    
    class Meta:
        model = Organizacion
        fields = '__all__'

    barrio = forms.ModelChoiceField(queryset=Barrio.objects.all())

class BusquedaLaboralForm(forms.ModelForm):   

    class Meta:
        model = BusquedaLaboral
        fields = '__all__'
    
    tecnologia = forms.ModelMultipleChoiceField(
        queryset=Tecnologia.objects.all(), widget=forms.CheckboxSelectMultiple)
    fechaApertura = forms.DateField()
    fechaCierre = forms.DateField()

