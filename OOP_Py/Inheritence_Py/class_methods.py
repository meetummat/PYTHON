# Class method in Python

class Employee():
    a = 1

    @classmethod  # classmethod is a decorator in Python
    def show(cls):
        # cls refers to the class itself.
        # So this will access the class value of a,
        # even if an instance has its own value of a.
        print(f"The class value of a is {cls.a}")


e = Employee()
e.a = 23  # this creates an instance attribute
e.show()