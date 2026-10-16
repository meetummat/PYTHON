# More file functions in python.

f = open("File_Input_Output_Py/file.txt") # if we dont specify the mode then the defalut mode is "r" read mode.

# lines = f.readlines() # it returns the list containing all the lines of files.
# print(lines, type(lines))

# line1 = f.readline() # it will access lines of files one by one as a string as many times we run this function that many lines we can access of that files.
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5, type(line5)) # if we try to print line which is not in file then it will return empty string.

# we can also use this in loop 
line = f.readline()
while line != "":
    print(line, type(line))
    line = f.readline()

f.close()