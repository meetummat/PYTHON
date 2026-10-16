# Using try with else.
# Using try with finally.


# try:
#     a = int(input("Hey!, Enter a number : "))
#     print(a)
#
# except Exception as e:
#     print(e)
#
# # If the try block runs without any error, the else block will execute.
# # The else block will NOT execute if an error occurs in the try block.
# else:
#     print("I am inside else")


# try:
#     a = int(input("Hey!, Enter a number : "))
#     print(a)
#
# except Exception as e:
#     print(e)
#
# # finally will always execute whether the try block succeeds
# # or an error occurs and the except block executes.
# finally:
#     print("I am inside finally")


def main():
    try:
        a = int(input("Hey!, Enter a number : "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        # finally will run even if the try or except block
        # executes a return statement.
        print("I am inside finally")


main()