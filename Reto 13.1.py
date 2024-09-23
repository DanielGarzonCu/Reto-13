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
