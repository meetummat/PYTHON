# Repeat program 4 for a list of such words to be censored.

words = ["donkey", "husband"]

with open("File_Input_Output_Py/File_Question_Py/donkey.txt", "r") as f:
    text = f.read().lower()

for word in words:
    text = text.replace(word, "#" * len(word))

with open("File_Input_Output_Py/File_Question_Py/donkey.txt", "w") as s:
    s.write(text)
