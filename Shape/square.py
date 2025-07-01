from Shape.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, vertices, is_regular: bool):
        if len(vertices) != 4:
            raise ValueError("Un cuadrado debe tener exactamente 4 vértices.")
        if not is_regular:
            raise ValueError("Un cuadrado debe ser una figura regular (is_regular=True).")
        super().__init__(vertices, is_regular)
