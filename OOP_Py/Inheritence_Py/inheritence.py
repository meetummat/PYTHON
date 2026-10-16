# Inheritance in Python

class Employee():
    company = "ITC"

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# This is single inheritance, where a child class inherits properties and methods
# from a single parent class.
class Programmer(Employee):
    # Employee is the Base/Parent class and Programmer is the Derived/Child class.
    # Programmer can access the attributes and methods of Employee
    # and can also have its own attributes and methods.

    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name of the Employee is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)