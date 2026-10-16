# Self Parameter in Python

class Employee:
    language = "Py"
    salary = 120000000

    # We can give any valid name instead of self,
    # but self is the standard name we use.
    def getInfo(self):  # self refers to the object which calls the function
        print(f"The language is : {self.language} and salary is : {self.salary}")

    def greet(self):  # even if we don't use any object property, we need self in an instance method
        print("Good Morning!")

    @staticmethod  # staticmethod is a decorator
    def anotherFun():  # static method does not take self automatically
        print("I am static method")


meet = Employee()
meet.language = "javascript"

meet.getInfo()
# This works like Employee.getInfo(meet),
# so the object is automatically passed as an argument.

meet.greet()
# This also works like Employee.greet(meet),
# so we need self to accept the object.

meet.anotherFun()
# It runs without self because it is a static method.