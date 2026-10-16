# How to write in a file?

st = "Hey Meet you are amazing!"

f = open("File_Input_Output_Py/file_write.txt", "w") # open funtion takes two arguments one is filename and other is mode to specify what operation we can perform on file.

f.write(st) # when we run this program file_write.py file made automatically with the text written in it.

f.close()