# Global keyword in Python
# The 'global' keyword is used to modify a global variable
# from inside a function.

a = 9
# a is a global variable because it is defined outside the function.


def fun():
    global a
    # Now Python knows that we want to use and modify the global variable a
    # instead of creating a new local variable.

    a = 3
    # This changes the value of the global variable a.

    print(a)


print(a)  # 9
fun()     # 3
print(a)  # 3