#  Write a program to filter a list of numbers which are divisible by 5.

l = [2, 5, 6, 10]

def divBy5(n):
    if n % 5 == 0:
        return True
    return False

print(list(filter(divBy5, l)))