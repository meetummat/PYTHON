# Write a program to find out whether a file is identical & matches the content of another file.

with open("File_Input_Output_Py/File_Question_Py/this.txt") as f:
    content1 = f.read()

with open("File_Input_Output_Py/File_Question_Py/poem.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("Yes these files are identical")
else:
    print("No these files are not identical")
