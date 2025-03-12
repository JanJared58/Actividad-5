def capturar_vector(nombre):
    vector = []
    longitud = int(input(f"Introduce la longitud del vector {nombre}: "))
    print(f"Introduce los elementos del vector {nombre}:")
    for i in range(longitud):
        elemento = int(input(f"Elemento {i+1}: "))
        vector.append(elemento)
    return vector

def producto_escalar(vector1, vector2):
    
    if len(vector1) != len(vector2):
        print("Los vectores no tienen la misma longitud. No se puede calcular el producto escalar.")
        return

    producto = 0
    for i in range(len(vector1)):
        producto += vector1[i] * vector2[i]
    
    print(f"El producto escalar de {vector1} y {vector2} es: {producto}")

vector1 = capturar_vector("1")
vector2 = capturar_vector("2")

if len(vector1) == len(vector2):
    producto_escalar(vector1, vector2)
else:
    print("Los vectores no tienen la misma longitud. No se puede calcular el producto escalar.")
