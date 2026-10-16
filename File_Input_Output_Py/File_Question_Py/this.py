# Write a program to make a copy of a text file “this. txt”

with open("File_Input_Output_Py/File_Question_Py/this.txt") as f:
    content = f.read()

with open("File_Input_Output_Py/File_Question_Py/this_copy.txt", "w") as f:
    f.write(content)