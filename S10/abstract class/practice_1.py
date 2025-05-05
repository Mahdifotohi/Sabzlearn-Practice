from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        """This method is for calculating employee salaries and must be implemented."""


class HourlyEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class SalariedEmployee(Employee):
    def __init__(self, annual_salary):
        self.annual_salary = annual_salary

    def calculate_salary(self):
        return self.annual_salary / 12


# Example usage
hourly_employee = HourlyEmployee(hourly_rate=20, hours_worked=160)
print("Hourly Employee Salary:", hourly_employee.calculate_salary())

salaried_employee = SalariedEmployee(annual_salary=60000)
print("Salaried Employee Monthly Salary:", salaried_employee.calculate_salary())
