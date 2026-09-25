# Loops in python.
# sometimes we want to repeat a set of statements in our program then we will use loops.

# for i in range (1, 6): # it uses the value as indexing 1 is included and 6 is not included.
#     print(i) # it will print values from 1 to 5

# range function generates the number from 0 to n-1.
for i in range(4): # it will automatically convert into (0,4) so it will goes from 0 to 3
    print(i)

# step size in for loop like the string slicing.
# range(start, stop, step)
# step tells how much i increases after each iteration
for i in range(0, 10, 2): # it will print with the gap of 2 now 
    print(i)

# using for loop in list
l = [1, 2, 4, 5 , 6, 7, 8]
# for i in range(0, len(l)): # we dont have to do (0, len(l)-1) because len(l) is already excluded.
#     print(l[i])

# or we can print also like
for i in l: # here i is an actuall element and stores the value of the list one by one and will print it.
    print(i)

# same for tuple
t = (1,3,5,6,7)
for i in t:
    print(i)

# even in the string
s = "Meet"
for i in s:
    print(i)