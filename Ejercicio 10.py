def capturar_conjunto(nombre):
    conjunto = set()
    n = int(input(f"Introduce el número de elementos del conjunto {nombre}: "))
    print(f"Introduce los elementos del conjunto {nombre}:")
    for _ in range(n):
        elemento = input("Elemento: ")
        conjunto.add(elemento)
    return conjunto

def interseccion_conjuntos(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

conjunto1 = capturar_conjunto("1")
conjunto2 = capturar_conjunto("2")

interseccion = interseccion_conjuntos(conjunto1, conjunto2)

print(f"La intersección de los conjuntos es: {interseccion}")
