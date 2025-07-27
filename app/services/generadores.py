import csv
import os

def generar_csv(nombre):
    ruta = f"{nombre}.csv"
    with open(ruta, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Nombre'])
        for i in range(1, 6):
            writer.writerow([i, f'Elemento {i}'])
    return os.path.abspath(ruta)
