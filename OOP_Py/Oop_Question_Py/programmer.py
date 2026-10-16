# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer():
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

m = Programmer("Meet", 1300000000, 232323)
print(m.name, m.salary, m.pin, m.company)
r = Programmer("Ronaldo", 1300000000, 232323)
print(r.name, r.salary, r.pin, r.company) 