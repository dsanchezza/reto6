from Shape.line import Line
from Shape.point import Point

class Shape:
    def __init__(self, vertices, is_regular: bool):
        if not all(isinstance(v, Point) for v in vertices): #Se verifica que todos los vértices sean instancias de Point
            raise TypeError("Todos los vértices deben ser instancias de la clase Point.")
        if len(vertices) < 3:
            raise ValueError("Un polígono debe tener al menos tres vértices.")
        if not isinstance(is_regular, bool): #Se verifica que el parámetro is_regular sea booleano
            raise TypeError("El parámetro 'is_regular' debe ser de tipo booleano.")

        self.vertices = vertices
        self.edges = []
        self.inner_angles = []
        self.is_regular = is_regular
        self.make_edges()

    def make_edges(self):
        for i in range(len(self.vertices) - 1):
            punto_inicio = self.vertices[i]
            punto_final = self.vertices[i + 1]
            lado = Line(punto_inicio, punto_final)
            self.edges.append(lado)
        punto_final = self.vertices[-1]
        punto_inicial = self.vertices[0]
        lado_final = Line(punto_final, punto_inicial)
        self.edges.append(lado_final)

    def compute_area(self):
        raise NotImplementedError #Este metodo debe ser implementado por las subclases

    def compute_perimeter(self):
        raise NotImplementedError

    def compute_inner_angles(self):
        raise NotImplementedError
