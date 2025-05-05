class Matrix:
    def __init__(self, a11, a12, a21, a22):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22

    def __add__(self, other):
        if isinstance(other, Matrix):
            return Matrix(
                self.a11 + other.a11, self.a12 + other.a12,
                self.a21 + other.a21, self.a22 + other.a22
            )
        raise ValueError("Addition is only supported between two Matrix objects.")

    def __sub__(self, other):
        if isinstance(other, Matrix):
            return Matrix(
                self.a11 - other.a11, self.a12 - other.a12,
                self.a21 - other.a21, self.a22 - other.a22
            )
        raise ValueError("Subtraction is only supported between two Matrix objects.")

    def __str__(self):
        return f"[{self.a11}, {self.a12}]\n[{self.a21}, {self.a22}]"


# Example usage:
m1 = Matrix(1, 2, 3, 4)
m2 = Matrix(5, 6, 7, 8)

print("Matrix 1:")
print(m1)

print("\nMatrix 2:")
print(m2)

print("\nAddition:")
print(m1 + m2)

print("\nSubtraction:")
print(m1 - m2)