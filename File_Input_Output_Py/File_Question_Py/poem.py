# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("File_Input_Output_Py/File_Question_Py/poem.txt") as f:
    if "twinkle" in f.read().lower():
        print('file contains the word "twinkle"')
    else:
        print('file does not contains the word "twinkle"')
