# Reto-13
## 1 Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
```ruby
def imprimir_valores_ascendente(diccionario):
    # Ordena y devuelve los valores del diccionario en orden ascendente
    valores = sorted(diccionario.values())
    return valores

if __name__ == "__main__":
    diccionario = {}  # Inicializa un diccionario vacío
    i = 1  # Contador para el número de elementos

    while True:  # Bucle infinito para ingresar elementos
        # Solicita al usuario la clave del nuevo elemento
        clave = input(f"Ingrese la clave del elemento {i} del diccionario (enter para continuar): ")
        if clave == "":  # Si el usuario no ingresa nada, se sale del bucle
            break

        # Solicita al usuario el valor correspondiente a la clave
        valor = input(f"Ingrese el valor de la clave '{clave}' del diccionario (enter para continuar): ")
        if valor == "":  # Si el usuario no ingresa nada, se sale del bucle
            break

        # Asigna el valor a la clave en el diccionario
        diccionario[clave] = valor
        i += 1  # Incrementa el contador

    # Llama a la función para obtener los valores ordenados
    resultado = imprimir_valores_ascendente(diccionario)
    print("Valores ordenados ascendentemente:")
    
    # Imprime cada valor ordenado
    for valor in resultado:  # Iterar directamente sobre resultado
        print(valor)
```
## 2 Desarrollar una funcion que reciba dos diccionarios como parametros y los mezcle
```ruby
import random
def mezclar_diccionarios(dic1, dic2):
    # Crear una lista de todas las claves de ambos diccionarios
    todas_claves = list(dic1.keys()) + list(dic2.keys())
    # Mezclar las claves de forma aleatoria
    random.shuffle(todas_claves)

    # Crear un nuevo diccionario para almacenar el resultado
    diccionario_mezclado = {}

    for clave in todas_claves:
        # Si la clave está en dic1, se añade al nuevo diccionario
        if clave in dic1:
            diccionario_mezclado[clave] = dic1[clave]
        # Si la clave no está en dic1 pero sí en dic2, se añade
        elif clave in dic2:
            diccionario_mezclado[clave] = dic2[clave]
        # Si la clave se repite se añade la del dic1
        elif clave in dic1 and clave in dic2:
            diccionario_mezclado[clave] = dic1[clave]

    return diccionario_mezclado

if __name__ == "__main__":
    dic1 = {}  # Inicializa un diccionario vacío
    dic2 = {}  # Inicializa un segundo diccionario vacío

    # Ingreso de datos para el primer diccionario
    i = 1  # Contador para el número de elementos
    while True:  # Bucle infinito para ingresar elementos
        clave1 = input(f"Ingrese la clave del elemento {i} del primer diccionario (enter para continuar): ")
        if clave1 == "":  # Si el usuario no ingresa nada, se sale del bucle
            break
        valor1 = input(f"Ingrese el valor de la clave '{clave1}' del primer diccionario (enter para continuar): ")
        if valor1 == "":  # Si el usuario no ingresa nada, se sale del bucle
            break
        dic1[clave1] = valor1
        i += 1  # Incrementa el contador

    # Ingreso de datos para el segundo diccionario
    j = 1  # Contador para el número de elementos
    while True:  # Bucle infinito para ingresar elementos
        clave2 = input(f"Ingrese la clave del elemento {j} del segundo diccionario (enter para continuar): ")
        if clave2 == "":  # Si el usuario no ingresa nada, se sale del bucle
            break
        valor2 = input(f"Ingrese el valor de la clave '{clave2}' del segundo diccionario (enter para continuar): ")
        if valor2 == "":  # Si el usuario no ingresa nada, se sale del bucle
            break
        dic2[clave2] = valor2
        j += 1  # Incrementa el contador

    # Llama a la función para mezclar los diccionarios después de haber llenado ambos
    diccionarios_mezclados = mezclar_diccionarios(dic1, dic2)

    # Imprime el diccionario mezclado
    print("Diccionario mezclado:")
    for clave, valor in diccionarios_mezclados.items():
        print(f"{clave}: {valor}")
```
## 3  Dado el JSON
```ruby
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "D��az Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["F�utbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```
### Cree un programa que lea de un archivo con dicho JSON 
 - Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
 - Imprima los nombres completos (nombre y apellidos) de las personas que esten en un rango de edades dado por el usuario.

```ruby
import json

# Datos en formato JSON
json_data = '''
{
    "jadiazcoronado": {
        "nombres": "Juan Antonio",
        "apellidos": "Díaz Coronado",
        "edad": 19,
        "colombiano": true,
        "deportes": ["Fútbol", "Ajedrez", "Gimnasia"]
    },
    "dmlunasol": {
        "nombres": "Dorotea Maritza",
        "apellidos": "Luna Sol",
        "edad": 25,
        "colombiano": false,
        "deportes": ["Baloncesto", "Ajedrez", "Gimnasia"]
    }
}
'''

def cargar_datos(json_data):
    """Carga datos JSON en un diccionario."""
    return json.loads(json_data)

def imprimir_nombres_por_deporte(data, deporte):
    """Imprime nombres de personas que practican un deporte específico."""
    for persona in data.values():
        if deporte in persona['deportes']:
            print(f"{persona['nombres']} {persona['apellidos']}")

def imprimir_nombres_por_edad(data, edad_min, edad_max):
    """Imprime nombres de personas dentro de un rango de edad específico."""
    for persona in data.values():
        if edad_min <= persona['edad'] <= edad_max:
            print(f"{persona['nombres']} {persona['apellidos']}")


if __name__ == "__main__":
    # Cargar los datos
    data = cargar_datos(json_data)

    # Solicitar entrada del usuario
    deporte_usuario = input("Ingrese el deporte: ")
    edad_minima = int(input("Ingrese la edad mínima: "))
    edad_maxima = int(input("Ingrese la edad máxima: "))

    # Imprimir resultados
    print("\nPersonas que practican", deporte_usuario)
    imprimir_nombres_por_deporte(data, deporte_usuario)

    print("\nPersonas con edad entre", edad_minima, "y", edad_maxima)
    imprimir_nombres_por_edad(data, edad_minima, edad_maxima)

```
## 4
### Dado el JSON:
```ruby
import json

# Cargar archivo
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString)
```
### imprimir 
 - fechas de alerta
 - tipo de alerta y las variables asociadas.
```ruby
import json
from datetime import datetime

# JSON del clima 
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
# Cargamos el contenido del JSON en una variable 'data' como un diccionario.
data = json.loads(jsonString)

# Definimos una función que se encargará de verificar alertas meteorológicas.
def verificar_alertas(data):
    # Diccionario que mapea los campos de alerta en el JSON con una descripción más clara.
    campos_alertas = {
        'alertAlertas': 'alerta',
        'alertPrecip': 'precipitación',
        'alertTmpMax': 'temperatura máxima',
        'alertTmpMin': 'temperatura mínima',
        'alertVelViento': 'viento'
    }

    # Iteramos sobre cada campo de alerta en 'campos_alertas'.
    for key, tipo_alerta in campos_alertas.items():
        # Dentro de cada campo de alerta, iteramos sobre cada día y el estado de la alerta para ese día.
        for dia, estado in data[key].items():
            # Si el estado de la alerta no es "-", significa que hay una alerta activa.
            if estado != "-":
                # Convertimos el timestamp UNIX (en segundos) a una fecha legible.
                fecha_unix = data['dt'][dia]
                fecha = datetime.utcfromtimestamp(fecha_unix).strftime('%Y-%m-%d')

                # Dependiendo del tipo de alerta, mostramos información relevante.
                # Si es una alerta de precipitación, mostramos el nivel de lluvia.
                if key == 'alertPrecip':
                    nivel_lluvia = data['prcp'][dia]  # Nivel de lluvia en mm
                    print(f"Alerta de {tipo_alerta} en {fecha}: nivel de lluvia {nivel_lluvia} mm")

                # Si es una alerta de viento, mostramos la velocidad del viento.
                elif key == 'alertVelViento':
                    velocidad_viento = data['velViento'][dia]  # Velocidad del viento en m/s
                    print(f"Alerta de {tipo_alerta} en {fecha}: velocidad {velocidad_viento} m/s")

                # Si es una alerta de temperatura máxima, solo indicamos que hay una alerta.
                elif key == 'alertTmpMax':
                    print(f"Alerta de {tipo_alerta} en {fecha}.")

                # Si es una alerta de temperatura mínima, también indicamos que hay una alerta.
                elif key == 'alertTmpMin':
                    print(f"Alerta de {tipo_alerta} en {fecha}.")

                # Si es una alerta general, mostramos que hay una alerta sin detalles adicionales.
                elif key == 'alertAlertas':
                    print(f"Alerta en {fecha}.")

# Llamamos a la función para verificar las alertas en el diccionario 'data'.
verificar_alertas(data)

```
## 5 A través de un programa conectese a al menos 3 API's 
 - obtenga el JSON, imprimalo y extraiga los pares de llave : valor.
```ruby
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
```
