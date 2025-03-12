def capturar_matriz(nombre):
    matriz = []
    print(f"Introduce los elementos de la matriz {nombre}:")
    for i in range(3):
        fila = []
        for j in range(3):
            elemento = int(input(f"Elemento ({i+1}, {j+1}): "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz1, matriz2):
    resultado = []
    for i in range(3):
        fila = []
        for j in range(3):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

matriz1 = capturar_matriz("1")
matriz2 = capturar_matriz("2")

resultado = sumar_matrices(matriz1, matriz2)

print("Resultado de la suma de las matrices:")
for fila in resultado:
    print(fila)
