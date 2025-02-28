import json
import requests

class Actividad1: 
    def __init__(self):
        self.ruta_static = "src/pad/static/"  

    def leer_api(self, url):
        response = requests.get(url)
        return response.json()

    def escribir_json(self):
        pass  

# crear instancia de clase Ingestiones 
ingestion = Actividad1()

# URL de API que no necesita autenticación 
url_api = "https://restcountries.com/v3.1/all"  

# con esta linea se obtiene la información de la API
datos_json = ingestion.leer_api(url_api)

# estas lineas imprimen los datos obtenidos
print("Esta es la ruta estática:", ingestion.ruta_static)
print("Datos JSON obtenidos:", json.dumps(datos_json, indent=4, ensure_ascii=False))
