# With statement
# The best way to open and close the file automatically is the with statement.

# f = open("File_Input_Output_Py/file.txt")
# print(f.read())
# f.close()

# same thing can be written using with statement. 
with open("File_Input_Output_Py/file.txt") as f:
    print(f.read())
    # with the with statement you dont have to explicitly close the file.
    # as we move out from the with statement file have been closed automatically.