from django.shortcuts import render
from .forms import EdadForm, TextoForm, CSVForm, ZonaHorariaForm
from .services.procesadores import calcular_edad, analizar_texto
from .services.generadores import generar_csv
import datetime, pytz

def calcular_edad_view(request):
    resultado = None
    form = EdadForm(request.POST or None)
    if form.is_valid():
        resultado = calcular_edad(form.cleaned_data['fecha_nacimiento'])
    return render(request, 'app/edad.html', {'form': form, 'resultado': resultado})

def analizar_texto_view(request):
    resultado = None
    form = TextoForm(request.POST or None)
    if form.is_valid():
        resultado = analizar_texto(form.cleaned_data['contenido'])
    return render(request, 'app/texto.html', {'form': form, 'resultado': resultado})

def generar_csv_view(request):
    resultado = None
    form = CSVForm(request.POST or None)
    if form.is_valid():
        resultado = generar_csv(form.cleaned_data['nombre_archivo'])
    return render(request, 'app/csv.html', {'form': form, 'resultado': resultado})

def obtener_tiempo_view(request):
    ahora_utc = datetime.datetime.now(pytz.utc)
    zonas = {
        "Madrid": ahora_utc.astimezone(pytz.timezone('Europe/Madrid')),
        "Nueva York": ahora_utc.astimezone(pytz.timezone('America/New_York')),
        "Tokio": ahora_utc.astimezone(pytz.timezone('Asia/Tokyo'))
    }
    return render(request, 'app/tiempo.html', {'zonas': zonas})
