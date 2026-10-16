# MODES OF OPENING A FILE

# r – open for reading
# w - open for writing
# a - open for appending
# + - open for updating.
# ‘rb’ will open for read in binary mode.
# ‘rt’ will open for read in text mode. (default)

# a - open for appending - will add the lines at the end of the file.

st = "Hey Ronaldo you are amazing!"

f = open("File_Input_Output_Py/file_write.txt", "a")

f.write(st) # this line will be added at the end of the string. And this line will be added as many times we run this program.
f.close()
