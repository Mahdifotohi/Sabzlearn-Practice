class PrintInfoMixin:
    def print_info(self):
        print(f"ClassName: {self.__class__.__name__}")
        print("Attributes:")
        for attr , value in self.__dict__.items():
            print(f"{attr}: {value}")

#Test class for PrintInfoMixin
class TestClass(PrintInfoMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Example usage
test_obj = TestClass("John", 30)
test_obj.print_info()