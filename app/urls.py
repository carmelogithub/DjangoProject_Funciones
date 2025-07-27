from django.urls import path
from . import views

urlpatterns = [
    path('calcular-edad/', views.calcular_edad_view),
    path('analizar-texto/', views.analizar_texto_view),
    path('generar-csv/', views.generar_csv_view),
    path('obtener-tiempo/', views.obtener_tiempo_view),
]
