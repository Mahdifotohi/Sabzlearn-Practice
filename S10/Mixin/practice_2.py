class MathOperationsMixin:
    def plus(self, x, y):
        return x + y
    def sub(self, x, y):
        return x - y
    def Multiply(self, x, y):
        return x * y
    def division(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Division by zero is not allowed.")
    