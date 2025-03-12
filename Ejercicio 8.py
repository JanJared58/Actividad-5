def capturar_punto(nombre):
    x = float(input(f"Introduce la coordenada x del punto {nombre}: "))
    y = float(input(f"Introduce la coordenada y del punto {nombre}: "))
    return (x, y)

def distancia_euclidiana(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2

    dx = x2 - x1
    dy = y2 - y1

    distancia = (dx ** 2 + dy ** 2) ** 0.5
    return distancia

punto1 = capturar_punto("1")
punto2 = capturar_punto("2")

distancia = distancia_euclidiana(punto1, punto2)

print(f"La distancia euclidiana entre {punto1} y {punto2} es: {distancia}")
