# Write a program to find the sum of first n natural numbers using while loop.

i = 1
sum = 0
n = int(input("Enter a number : "))
while(i <= n):
    sum += i
    i +=1

print(sum)