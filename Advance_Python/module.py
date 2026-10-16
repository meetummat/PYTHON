def myfunc():
    print("Hello World!")


# myfunc()
# print(__name__)
# If we run this file directly, __name__ will contain "__main__".
# If this file is imported into another file, __name__ will contain
# the name of this file instead.


if __name__ == "__main__":
    # This block will run only when this file is directly executed.
    # It will not run automatically when this file is imported into another file.

    print("We are directly running this code")
    myfunc()
    print(__name__)