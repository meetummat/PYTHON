# Constructor in Python

class Employee:
    language = "Py"
    salary = 120000000

    def __init__(self, name, salary, language):
        # __init__ is a special method in Python called a dunder method.
        # Dunder methods are methods that start and end with "__".
        # __init__ is automatically called when an object is created.

        self.name = name  # these are instance attributes
        self.salary = salary
        self.language = language

        print("I am creating an object")
        # We didn't call __init__ ourselves.
        # It is automatically called when we create an object.


meet = Employee("Meet", 1300000, "javascript")
# We are passing the values to __init__ while creating the object.

print(meet.name, meet.salary, meet.language)


# If we have parameters in __init__ other than self,
# we have to provide those values when creating the object.
# Otherwise, it will give an error.

# ronaldo = Employee()
# We have made another object here, so __init__ will be called again.
# But this will give an error because name, salary and language are required.