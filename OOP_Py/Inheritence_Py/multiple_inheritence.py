# Multiple Inheritance in Python
# When a child class inherits from more than one parent class.

class Employee():
    company = "ITC"
    name = "Meet"
    salary = 12343434

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


class Coder:
    language = "python"

    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")


class Programmer(Employee, Coder):
    # This class is inheriting from both Employee and Coder,
    # so this is called multiple inheritance.

    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name of the Employee is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguage()  # The child class can access methods from both parent classes.
b.showLanguage()