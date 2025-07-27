from datetime import date, datetime

def calcular_edad(fecha_nac):
    hoy = date.today()
    edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
    return edad

def analizar_texto(texto):
    lineas = texto.split('\n')
    palabras = texto.split()
    return {
        "líneas": len(lineas),
        "palabras": len(palabras),
        "caracteres": len(texto)
    }
