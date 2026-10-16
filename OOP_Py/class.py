# Classes in Python

class Employee:  # class syntax
    name = ""
    language = "Py"  # this is a class attribute
    salary = 120000000
    # class ends here


meet = Employee()  # meet is an object of the Employee class
meet.name = "Meet"  # this creates an instance attribute for the meet object

# Instance attribute takes preference over the class attribute during retrieval.
# It does not change the class attribute; it only creates/sets an instance attribute.

print(Employee.name)  # this will still have the same value as we set in the class.
print(meet.name, meet.language, meet.salary)  # access class/instance attributes using an object


ronaldo = Employee()  # another object of the Employee class
ronaldo.name = "Ronaldo"
print(ronaldo.name, ronaldo.salary, ronaldo.language)