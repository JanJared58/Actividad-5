def capturar_conjunto(nombre):
    conjunto = set()
    n = int(input(f"Introduce el número de elementos del conjunto {nombre}: "))
    print(f"Introduce los elementos del conjunto {nombre}:")
    for _ in range(n):
        elemento = input("Elemento: ")
        conjunto.add(elemento)
    return conjunto

def union_conjuntos(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)

conjunto1 = capturar_conjunto("1")
conjunto2 = capturar_conjunto("2")

union = union_conjuntos(conjunto1, conjunto2)

print(f"La unión de los conjuntos es: {union}")
