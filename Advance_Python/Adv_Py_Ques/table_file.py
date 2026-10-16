# Store the multiplication tables generated in problem 3 in a file named Tables.txt


n = int(input("Enter a number : "))
table = [n * i for i in range(1, 11)]

# with open("Advance_Python/Adv_Py_Ques/Tables.txt", "w") as f:
#     f.write(str(table))

with open("Advance_Python/Adv_Py_Ques/Tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")