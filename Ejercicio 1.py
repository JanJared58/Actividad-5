def crear_matriz(n, m):

    matriz = []

    for i in range(n):
        
        fila = []
        
        for j in range(m):
           
            valor = (i + j) % 2
            fila.append(valor)
        
        matriz.append(fila)
    
    return matriz

n = int(input("Introduce el número de filas (n): "))
m = int(input("Introduce el número de columnas (m): "))

matriz = crear_matriz(n, m)

for fila in matriz:
    print(fila)
