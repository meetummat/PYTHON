# Property decorators in Python

# Encapsulation:
# Encapsulation means keeping data and the methods that work with that data together
# and controlling how the data can be accessed or changed.

# Abstraction:
# Abstraction means hiding unnecessary implementation details
# and showing only the important part to the user.
# Here, we don't need to know how the name is split and stored internally.
# We can simply use e.name to get the full name and e.name = "Meet Ummat" to set it.


class Employee():
    a = 1

    @classmethod
    def show(cls):
        # cls refers to the class itself.
        # cls.a accesses the class attribute a.
        print(f"The class value of a is {cls.a}")


    @property
    def name(self):
        # This is called a getter.
        # @property allows us to use this method like an attribute.
        # So we can write e.name instead of e.name().
        return f"{self.fname} {self.lname}"


    @name.setter
    def name(self, value):
        # This is called a setter.
        # It runs when we assign a value to e.name.
        # For example: e.name = "Meet Ummat"

        # split(" ") splits the string wherever there is a space.
        # "Meet Ummat".split(" ") gives ["Meet", "Ummat"]
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()

e.a = 23
# This creates an instance attribute a.
# It does not change the class attribute Employee.a.


e.name = "Meet Ummat"
# The setter runs here.
# value = "Meet Ummat"
# value.split(" ") gives ["Meet", "Ummat"]
# [0] gives "Meet", so self.fname = "Meet"
# [1] gives "Ummat", so self.lname = "Ummat"


print(e.name)
# The getter runs here.
# It returns "Meet Ummat" by combining fname and lname.


e.show()
# This is a class method.
# cls.a refers to the class attribute, so it prints 1 and not 23.