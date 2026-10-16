# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator():
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is : {self.n*self.n}")

    def cube(self):
        print(f"The cube is : {self.n*self.n*self.n}")

    def sqroot(self):
        print(f"The square root is : {self.n**(1/2):.2f}")

    # Add a static method in problem 2, to greet the user with hello.
    @staticmethod
    def hellouser():
        print("Hello there!")

a = Calculator(5)
a.hellouser()
a.square()
a.cube()
a.sqroot()