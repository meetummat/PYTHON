# Write a class ‘Complex’ to represent complex numbers,
# along with overloaded operators '+' and '*' which adds and multiplies them.


class Complex:
    def __init__(self, r, i):
        # r represents the real part and i represents the imaginary part.
        self.r = r
        self.i = i


    # Formula to add two complex numbers.
    def __add__(self, c2):
        # When we write c1 + c2, Python calls c1.__add__(c2).
        # self represents c1 and c2 represents the second complex number.
        #
        # For example:
        # (1 + 2i) + (3 + 4i)
        # = (1 + 3) + (2 + 4)i
        # = 4 + 6i
        #
        # We return a new Complex object containing the result.
        return Complex(self.r + c2.r, self.i + c2.i)


    # Formula to multiply two complex numbers.
    def __mul__(self, c2):
        # When we write c1 * c2, Python calls c1.__mul__(c2).
        #
        # Formula:
        # (a + bi)(c + di)
        # = (ac - bd) + (ad + bc)i

        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r

        # Return a new Complex object containing the result.
        return Complex(real_part, imag_part)


    # __str__ decides how the object will look when we print it.
    def __str__(self):
        # It returns the complex number in the form: a + bi.
        return f"{self.r} + {self.i}i"


c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(c1 + c2)
# This calls c1.__add__(c2)
# Output: 4 + 6i

print(c1 * c2)
# This calls c1.__mul__(c2)
# Output: -5 + 10i