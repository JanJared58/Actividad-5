import math

def polar_a_cartesianas(coordenada_polar):

    r, theta = coordenada_polar
    theta = math.radians(theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

coordenada_polar = (5, 45)  
coordenada_cartesiana = polar_a_cartesianas(coordenada_polar)

print(f"La coordenada polar {coordenada_polar} convertida a coordenada cartesiana es: {coordenada_cartesiana}")
