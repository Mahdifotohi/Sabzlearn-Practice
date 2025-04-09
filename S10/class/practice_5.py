class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def replace_salary(self, amount):
        self.salary += amount

    def get_info(self):
        return f"Name: {self.name}, Salary: {self.salary}."


# Example usage:
employee_info = Employee("MahdiFotohi", 5000)
employee_info.replace_salary(200)
print(employee_info.get_info())
