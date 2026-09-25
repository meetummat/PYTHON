# functions in python:-
# function is a group of statements performing a specific task.

# how to define a function
def avg(): # this is a function defination.
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    c = int(input("Enter third number : "))

    average = (a+b+c)/3
    print(f"Average is {average:.2f}")
    # here the function ends.

avg() # this is a function call, we use it when we want to execute the code of the function.
# Through a function call, a function can be executed any number of times anywhere in the program.

# function to greet
def greet():
    name = input("Enter your name : ")
    print(f"Hello {name}")

greet()