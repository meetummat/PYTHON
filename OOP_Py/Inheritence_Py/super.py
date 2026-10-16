# super method in Python
# super() is used to access methods of the parent class from the derived class.


class Employee():
    def __init__(self):
        print("Constructor of Employee")

    a = 1


class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")

    b = 2


class Manager(Programmer):
    def __init__(self):
        super().__init__()
        # This calls the __init__ method of the parent class (Programmer).
        print("Constructor of Manager")

    c = 3


o = Manager()
print(o.a, o.b, o.c)