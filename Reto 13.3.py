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
