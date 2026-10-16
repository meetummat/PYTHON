# Walrus operator in Python -> :=
# It allows us to assign a value to a variable as part of an expression.

# Without the walrus operator:
# n = [1, 2, 3, 4, 5]
# if len(n) > 3:
#     print(f"List is too long ({len(n)} elements, expected <=3)")

# With the walrus operator, we can assign the value
# and use it in the condition at the same time.
# Here n will store the length of the list.
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <=3)")