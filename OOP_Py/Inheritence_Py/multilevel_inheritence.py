# Multilevel Inheritance in Python.
# When a child class becomes the parent class of another child class.


class Employee():
    a = 1


class Programmer(Employee):
    b = 2


class Manager(Programmer):
    c = 3


o = Employee()
print(o.a)  # Prints the a attribute of the Employee class.
# print(o.b)  # Shows an error because Employee does not have b.


o = Programmer()
print(o.a, o.b)  # Programmer can access attributes of Employee and Programmer.
# print(o.c)  # Shows an error because Programmer does not have c.


o = Manager()
print(o.a, o.b, o.c)
# Manager can access attributes of Manager, Programmer and Employee.
# This is called multilevel inheritance.