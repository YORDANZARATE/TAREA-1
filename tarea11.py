#Crear un programa que incluya una matriz dimensional con valores numericos (3x3)

matriz=[ [10,30,20],
         [40,60,50],
         [90,70,80]
         ]
valor_buscado =10
if any(valor_buscado in fila for fila in matriz):
    print(f"se encontro {valor_buscado}")
else:
    print(f" {valor_buscado}")

#Implementa una función que ordene una fila específica de la matriz en orden ascendente

matriz.sort(key=lambda  fila: max(fila))

#mostrar la matriz ordenada

print("\nmatriz ordenada por valor en cada fila:")
for fila in matriz:
    print(fila)