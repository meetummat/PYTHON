# while loops

i = 1
# it will check the condition first to execute if the condition is not true then it will not execute.
# and it will continue to execute till the condition is true.
# if the contidion is always true then it will become infinite loop, which is not good.
while(i < 6): # in this we have to specify condition first, it will also print values from 1 to 5
    print(i)
    i += 1
# End of while loop.

# print "Meet" five times.
i =1
while(i <= 5):
    print("Meet")
    i += 1

# write a program to print content of list using while loop.
l = [1, 2, 4, 5 , 6, 7, 8]
i = 0
while(i < len(l)):
    print(l[i])
    i += 1