# Write a python program using function to convert Celsius to Fahrenheit.
# formula of celcius to fahrenhiet is c/5 = (f-32)/9

def fah_to_cel(f):
    c = 5*(f-32)/9
    return c

f = int(input("Enter temperature : "))
print(f"{fah_to_cel(f):.2f}c")

def cel_to_fah(c):
    f = c*9/5 + 32
    return f

c = float(input("Enter temperature : "))
# print(f"{cel_to_fah(c):.2f}f")
print(f"{round(cel_to_fah(c), 2)}f") 
# round(value, ndigits) rounds a number to the specified number of decimal places.