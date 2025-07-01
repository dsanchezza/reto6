from Shape.shape import Shape

class Rectangle(Shape):
    def __init__(self, vertices, is_regular: bool):
        if len(vertices) != 4:
            raise ValueError("Un rectángulo debe tener exactamente 4 vértices.")
        super().__init__(vertices, is_regular)

    def compute_area(self):
        lado1 = self.edges[0].length
        lado2 = self.edges[1].length
        return lado1 * lado2

    def compute_perimeter(self):
        return sum(edge.length for edge in self.edges)

    def compute_inner_angles(self):
        return [90.0] * 4
