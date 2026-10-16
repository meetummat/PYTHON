# Operator Overloading in Python

# Operators in Python can be overloaded using dunder methods.
# Operator overloading means we can define what an operator
# like +, -, *, etc. should do when it is used with our objects.


class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        # __add__ is a dunder method for the + operator.
        # When we write n + m, Python internally calls:
        # n.__add__(m)
        #
        # Here self refers to n and num refers to m.
        # So self.n = 1 and num.n = 2.
        # Therefore, it returns 1 + 2 = 3.
        return self.n + num.n

    def __str__(self):
        # __str__ is a dunder method.
        # It decides what should be returned when we use print()
        # with an object.
        #
        # It should return a string.
        return f"Number is {self.n}"

    def __len__(self):
        # __len__ is a dunder method.
        # It decides what should be returned when we use len()
        # with an object.
        #
        # It should return an integer.
        return len(str(self.n))


n = Number(1)
m = Number(2)

print(n + m)
# This calls n.__add__(m)
# Output: 3

print(n)
# This calls n.__str__()
# Output: Number is 1

print(len(n))
# This calls n.__len__()
# self.n is 1
# str(self.n) becomes "1"
# "1" has 1 character, so output is 1