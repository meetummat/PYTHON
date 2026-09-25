# Operators in python.

# 1. Arithmetic operators: +, -, *, /, //, **, %.
a = 3+6 # 3 and 6 are operands, "+" is a operator.
b = 8-3
c = 3*7
d = 9/3 # gives result in floating point number.
e = 9//3 # gives result in integer
f = 2**3 # will print 2^3, exponent
g = 10%4 # will print remainder

# /----------------------------------------------------------

# 2. Assignment operators: =, +=, -=, *=, /=, %=, **=.
h = 3 # assign 3 in h.
h += 5
print(h) # add 5 in h's previous value and then will assign that to h.
h -= 2
print(h) # sub 2 in h's previous value.
h*= 2
print(h) # multiply 2 in h's previous value.

h/= 3    # can also use h = h//3 for integer division.
print(h) # divide 3 in h's previous value.
h %= 2
print(h) # remainder of h's previous value.

h**= 3
print(h) # h's previous value to the power of 3.

# /----------------------------------------------------------

# 3. Comparison operators: ==, !=, >, <, >=, <=.
# Always returns booleand value.
print( a==b ) # will return true if its true and false if its false.
print( a!=b ) # != not equal to.
print( a>b )
print( c<d )
print( c>=f )
print( 5>=5 )

# /----------------------------------------------------------

# 4. Logical operators: and, or, not

# or :- If any one is true it will reutrn true.
# Truth table of or :-
print("True or False is : ", True or False) 
print("True or True is : ", True or True)
print("False or True is : ", False or True)
print("False or False is : ", False or False)

print() # to print the line.

# and :- If anyone is false return false.
# Truth table of and :-
print("True and False is : ", True and False) 
print("True and True is : ", True and True)
print("False and True is : ", False and True)
print("False and False is : ", False and False)

print()

# not :- operates on only one operand, convert true to false and false to true.
# # Truth table of not:-
print("not of False is : ", not(False)) 
print("not of True is : ", not(True))

# /----------------------------------------------------------