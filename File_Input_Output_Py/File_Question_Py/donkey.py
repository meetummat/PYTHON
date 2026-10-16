# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file. 

# with open("File_Input_Output_Py/File_Question_Py/donkey.txt", "r") as f:
#     text = f.read().lower()
    
# with open("File_Input_Output_Py/File_Question_Py/donkey.txt", "w") as s:
#     if "donkey" in text:
#         newtext = text.replace("donkey", "######")
#         s.write(newtext)

# another approach (better approach)
word = "donkey"

with open("File_Input_Output_Py/File_Question_Py/donkey.txt", "r") as f:
    text = f.read().lower()

newtext = text.replace("donkey", "######")

with open("File_Input_Output_Py/File_Question_Py/donkey.txt", "w") as s:
    s.write(newtext)
