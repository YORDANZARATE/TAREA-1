def bubble_sort(arr):
    """
    Ordena un arreglo en orden ascendente utilizando el algoritmo Bubble Sort.
    """
    n = len(arr)
    for i in range(n):
        # Flag para verificar si hubo algún intercambio
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambiar si el elemento actual es mayor que el siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Si no hubo intercambios, el arreglo ya está ordenado
        if not swapped:
            break


def imprimir_matriz(matriz):
    """
    Imprime una matriz en formato de tabla.
    """
    for fila in matriz:
        print(fila)


def ordenar_fila(matriz, fila_index):
    """
    Ordena una fila específica de la matriz en orden ascendente.
    """
    if fila_index < 0 or fila_index >= len(matriz):
        raise IndexError("Índice de fila fuera de rango")

    # Aplicar Bubble Sort a la fila seleccionada
    bubble_sort(matriz[fila_index])


def main():
    # Definir una matriz bidimensional 3x3
    matriz = [
        [12, 5, 8],
        [1, 14, 7],
        [9, 3, 6]
    ]

    print("Matriz Original:")
    imprimir_matriz(matriz)

    # Índice de la fila que se desea ordenar (por ejemplo, la fila 1)
    fila_a_ordenar = 1

    # Ordenar la fila específica
    ordenar_fila(matriz, fila_a_ordenar)

    print("\nMatriz después de ordenar la fila {}:".format(fila_a_ordenar))
    imprimir_matriz(matriz)


if __name__ == "__main__":
    main()



