def capturar_matriz():
    matriz = []
    filas = int(input("Introduce el número de filas de la matriz: "))
    columnas = int(input("Introduce el número de columnas de la matriz: "))
    print("Introduce los elementos de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Elemento ({i+1}, {j+1}): "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

def encontrar_elemento(matriz, elemento):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == elemento:
                return (i, j)
    return None

matriz = capturar_matriz()

elemento = int(input("Introduce el elemento a buscar en la matriz: "))

posicion = encontrar_elemento(matriz, elemento)
if posicion:
    print(f"El elemento {elemento} se encuentra en la posición (fila, columna): {posicion}")
else:
    print(f"El elemento {elemento} no está presente en la matriz.")
