# Exception Handling in Python
# It is used to handle errors so that the program does not crash
# and we can show a suitable message to the user.


try:
    # First, Python will run the code inside the try block.
    # If there is no error, the except blocks will be skipped.
    # If an error occurs, Python will look for a matching except block.

    a = int(input("Hey!, Enter a number : "))
    print(a)


except ValueError as v:
    # This block will execute if a ValueError occurs.
    # For example, if the user enters "hello" instead of a number.
    # v stores the error message.
    print("Heyyy!")
    print(v)


except Exception as e:
    # This is a general exception block.
    # It can handle many types of errors that are not handled
    # by the previous specific except blocks.
    # e stores the error message.
    print(e)


print("Thank you!")
# This code will execute even if an error occurred inside try,
# because the error was handled by the except block.