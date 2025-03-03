import json
import requests
import os

class Actividad1: 
    def __init__(self):
        self.ruta_static = "src/pad/static/txt/"  
        os.makedirs(self.ruta_static, exist_ok=True)  

    def leer_api(self, url):
        response = requests.get(url)
        return response.json()

    def escribir_json(self, datos, nombre_archivo="paises_api.json"):
        ruta_completa = os.path.join(self.ruta_static, nombre_archivo)
        with open(ruta_completa, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"Archivo JSON guardado en: {ruta_completa}")

# Crear instancia de la clase
ingestion = Actividad1()

# URL de API que no necesita autenticación 
url_api = "https://restcountries.com/v3.1/all"  

# obtiene los datos de la API
datos_json = ingestion.leer_api(url_api)

# imprime datos obtenidos
print("Esta es la ruta estática:", ingestion.ruta_static)
print("Datos JSON obtenidos:", json.dumps(datos_json, indent=4, ensure_ascii=False))

# garda datos en un archivo JSON
ingestion.escribir_json(datos_json)
