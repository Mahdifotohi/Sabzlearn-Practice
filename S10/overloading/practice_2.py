
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


# Example usage:
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

print("Addition:", c1 + c2)  # Output: 4 + 6i
print("Subtraction:", c1 - c2)  # Output: 2 + 2i
print("Multiplication:", c1 * c2)  # Output: -5 + 10i