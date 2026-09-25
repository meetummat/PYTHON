# Conditionals statements in python

# a = int(input("Enter your age : "))

# when if condition is true then if block will execute when if condition is false then else block will execute.
# this is if else ladder.
# if a > 18:
#     print("Can vote")
# else:
#     print("can not vote")


# if elif else 
# first it will check if condition if that is not true then it will check elif condition if that is also not true then it will execute else block.
# we can use multiple elif in program.
# it is also known as if elif else ladder.
age = int(input("Enter you age : "))
if (age > 0 and age < 18):
    print("Child")

elif age <= 0:
    print("Please enter valid age")

elif (age >= 18 and age <= 60):
    print("Adult")

else:
    print("Old")

print("End of program")
