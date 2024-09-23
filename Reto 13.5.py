import requests
import json

def obtener_datos_api(url, headers=None):
    # Realizamos una solicitud a la API y manejamos los errores
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(f"Datos de la API {url}:")
            print(json.dumps(data, indent=2))  # Imprimir el JSON formateado
            return data
        else:
            print(f"Error al acceder a la API {url}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

# API de Trivia (Open Trivia Database)
url_trivia = 'https://opentdb.com/api.php?amount=1'
# API de Chistes (JokeAPI)
url_joke = 'https://v2.jokeapi.dev/joke/Any'
# API de Gatos (The Cat API)
url_cat = 'https://api.thecatapi.com/v1/images/search'

# Diccionario con las URLs de las APIs
urls_apis = {
    'Trivia': url_trivia,
    'Chistes': url_joke,
    'Gatos': url_cat
}

# Iteramos sobre las APIs para obtener los datos
for nombre_api, url in urls_apis.items():
    print(f"\nConsultando {nombre_api}...")
    obtener_datos_api(url)

