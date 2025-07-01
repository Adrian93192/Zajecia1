class Matrix:
    def __init__(self, a, b, c, d):
        # Macierz reprezentowana jako 2x2
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        # Dodawanie macierzy element po elemencie
        return Matrix(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d
        )

    def __mul__(self, other):
        # Mnożenie macierzy 2x2
        return Matrix(
            self.a * other.a + self.b * other.c,
            self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c,
            self.c * other.b + self.d * other.d
        )

    def __str__(self):
        # Czytelna reprezentacja macierzy
        return f"[{self.a}, {self.b};\n {self.c}, {self.d}]"

    def __repr__(self):
        # Techniczna reprezentacja (do debugowania)
        return f"M({self.a}, {self.b}; {self.c}, {self.d})"

# Przykład użycia
# m1 = Matrix(1, 2, 3, 4)
# m2 = Matrix(2, 0, 1, 2)
# print(m1 + m2)
# print(m1 * m2)
