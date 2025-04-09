class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Example usage:
student = Student("John Doe", 20)
student.add_grade(15)
student.add_grade(20)
print(student.calculate_average())  # Output: 17.5