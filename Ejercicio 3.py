def producto_escalar(vector1, vector2):

    if len(vector1) != len(vector2):
        raise ValueError("Los vectores deben tener la misma longitud")
    
    producto = sum(x * y for x, y in zip(vector1, vector2))
    
    return producto

# Ejemplo de uso
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
resultado = producto_escalar(vector1, vector2)

print(f"El producto escalar de {vector1} y {vector2} es: {resultado}")
