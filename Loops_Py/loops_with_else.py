# We can use loops with else statement or with the if else statements.

l = [1, 2, 4, 5 , 6, 7, 8]

for i in l:
    print(i)
else:
    print("done") # after completing the work of for loop it will execute the else statement.
    # else executes when the loop finishes if the loop stopped using break the else block will not execute.

# same with while
i = 0 
while(i < len(l)):
    print(l[i])
    i += 1
else:
    print("done")