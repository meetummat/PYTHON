#  Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals(): # class name should me singular but as a problem statement we can make it plural.
    def __init__(self):
        print("This is a animal class")

class Pets(Animals):
    def __init__(self):
        super().__init__()
        print("This is a pet class")

class Dog(Pets):
    def __init__(self):
        super().__init__()
        print("This is a dog class")

    @staticmethod
    def bark():
        print("The dog barks")

a = Dog()
a.bark()