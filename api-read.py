#!/usr/bin/env python3

#from https://chatgpt.com/share/67af674c-c9e8-8002-9a34-223092682d1d
import requests
#import os

# URL de la API a la que haremos la solicitud
url = "https://services.swpc.noaa.gov/json/goes/primary/xrays-6-hour.json"

# Realizar una solicitud GET
response = requests.get(url)
#os.env("MY_TOKEN")
# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Convertir la respuesta a formato JSON (si la API devuelve JSON)
    data = response.json()
    print("Datos recibidos:")
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)  # Mostrar el contenido de la respuesta en caso de error
