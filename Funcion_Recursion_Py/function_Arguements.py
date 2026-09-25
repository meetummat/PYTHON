# Functions with Arguements
# Parameter → variable defined in function
# Argument → actual value passed to function
# return → sends a value back from function
# Default parameter → value used when no argument is provided

# this is how we use arguements in the function.
def goodDay(name, ending): # here name and ending are parameters
    print(f"Good Day {name} {ending}")
    return "done" # a function can return a value which can be used after storing in any variable.

a = goodDay("Meet", "Thank you") # "Meet" and "Thank you" are arguements going to parameter of the function.
print(a) # a has the return value of the function which will now print.
# if function is not returning anything then if we try to store funciton in variable it will store None. 


# Default Parameters.
# We can have a value as default as default argument in a function.
def goodDay(name, ending = "Thanks"): # now it will take Thanks as default value of ending, if we give other value through arguement then it will take that value.
    print(f"Good Day {name} {ending}")

goodDay("Meet")
goodDay("Meet", "Thank you")