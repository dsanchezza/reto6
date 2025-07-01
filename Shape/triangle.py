import math
from Shape.shape import Shape

class Triangle(Shape):
    def __init__(self, vertices, is_regular: bool):
        if len(vertices) != 3:
            raise ValueError("Un triángulo debe tener exactamente 3 vértices.") #Se verifica que haya 3 vértices para formar un triángulo
        super().__init__(vertices, is_regular)

    def compute_area(self):
        a, b, c = [edge.length for edge in self.edges]
        s = (a + b + c) / 2  # semiperímetro
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def compute_perimeter(self):
        return sum(edge.length for edge in self.edges)

    def compute_inner_angles(self):
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length
        angulo_a = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        angulo_b = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
        angulo_c = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
        self.inner_angles = [math.degrees(angulo_a), math.degrees(angulo_b), math.degrees(angulo_c)]
        return self.inner_angles

class TriRectangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices, is_regular=False)

class Scalene(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices, is_regular=False)

class Equilateral(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices, is_regular=True)

class Isosceles(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices, is_regular=False)