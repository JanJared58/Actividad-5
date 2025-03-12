def capturar_matriz():

    matriz = []
    print("Introduce los elementos de la matriz (5x5):")
    for i in range(5):
        fila = []
        for j in range(5):
            elemento = int(input(f"Elemento ({i+1}, {j+1}): "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

def sumar_diagonales(matriz):
    suma_principal = 0
    suma_secundaria = 0
    for i in range(5):
        suma_principal += matriz[i][i]
        suma_secundaria += matriz[i][4-i]
    return suma_principal, suma_secundaria

matriz = capturar_matriz()

suma_principal, suma_secundaria = sumar_diagonales(matriz)

print(f"Suma de la diagonal principal: {suma_principal}")
print(f"Suma de la diagonal secundaria: {suma_secundaria}")
