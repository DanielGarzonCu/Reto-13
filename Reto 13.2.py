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
