import math

class Point:
    def __init__(self, x: int, y: int):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)): #Se verifica que las coordenadas sean números
            raise TypeError("Las coordenadas deben ser números (int o float).")
        self.x = x
        self.y = y

    def compute_distance(self, point: 'Point'): #Se verifica que el argumento recibido sea una instancia de la clase Point
        if not isinstance(point, Point):
            raise TypeError("El argumento debe ser una instancia de la clase Point.")
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
