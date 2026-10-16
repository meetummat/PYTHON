# Write a python program to rename a file to “renamed_by_ python.txt.

with open("File_Input_Output_Py/File_Question_Py/old.txt") as f:
    content = f.read()

with open("File_Input_Output_Py/File_Question_Py/renamed_by_python.txt", "w") as f:
    f.write(content)

# after copying we can delete old file by ourself or by os or shutil module.