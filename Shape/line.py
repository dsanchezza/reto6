from Shape.point import Point

class Line:
    def __init__(self, start_point, end_point):
        if not isinstance(start_point, Point) or not isinstance(end_point, Point): #Se valida que ambos puntos sean válidos
            raise TypeError("Los puntos de inicio y fin deben ser instancias de Point.")
        self.start_point = start_point
        self.end_point = end_point
        self.calculate_length()

    def calculate_length(self):
        self.length = self.start_point.compute_distance(self.end_point) #Se calcula la longitud de la línea utilizando la distancia entre puntos
