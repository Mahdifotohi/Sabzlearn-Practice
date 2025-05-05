from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    @abstractmethod
    def greet(self):
        """This method must be written."""

    @abstractmethod
    def introduce(self):
        """This method must be written."""


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "Student")

    def greet(self):
        print(f"Hi, iam {self.name}.")

    def introduce(self):
        print(f"I am {self.name}, {self.age} years old, and I am a {self.role}.")


class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "Teacher")

    def greet(self):
        print(f"Hi, iam {self.name}.")

    def introduce(self):
        print(f"I am {self.name}, {self.age} years old, and I am a {self.role}.")


# Example usage
student = Student("ali", 20)
teacher = Teacher("Rezai", 35)

student.greet()
student.introduce()

teacher.greet()
teacher.introduce()
