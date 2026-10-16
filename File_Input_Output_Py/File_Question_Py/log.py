# Write a program to mine a log file and find out whether it contains ‘python’.

# with open("File_Input_Output_Py/File_Question_Py/log.txt") as f:
#     python = f.read().lower()

# if "python" in python:
#     print("It contains Python")
# else:
#     print("It does not contain Python")

# Write a program to find out the line number where python is present from ques 6.

with open("File_Input_Output_Py/File_Question_Py/log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"Yes python is present. Line no: {lineno}")
        break
    lineno += 1
else:
    print("No python is not present")

