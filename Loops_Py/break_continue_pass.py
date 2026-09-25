# break continue and pass statements in python.


# break → immediately exits the current loop.
for i in range(10):
    if i == 5:
        break # now it will print from 0 to 4 when i will be 5 the loop will break.
    print(i)


# continue → skips the current iteration and moves to the next iteration.
for i in range(10):
    if i == 5:
        continue # now it will print from 0 to 9 when i will be 5 the loop will skip it, it will now print 5. Simply it will not execute the code written after continue in loop.
    print(i)


# pass → does nothing; used as a placeholder where Python requires a statement.
# pass is a null statement in python.
for i in range(10):
    pass # without pass if we want to code more in this file it will give error.
    # if we dont know what to do in it and wants to leave it empty for future use then we can use pass and code further.

# Nested loops → a loop inside another loop.
for i in range(1, 3):
    for j in range(1, 3):
        print(f"i={i}, j={j}") # Used in matrix traversal, combinations, pattern printing. break/continue affect only the innermost loop in which they are used.
