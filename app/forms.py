# acciones/forms.py
from django import forms

class EdadForm(forms.Form):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class TextoForm(forms.Form):
    contenido = forms.CharField(widget=forms.Textarea)

class CSVForm(forms.Form):
    nombre_archivo = forms.CharField()

class ZonaHorariaForm(forms.Form):
    pass  # sin campos, solo un botón
