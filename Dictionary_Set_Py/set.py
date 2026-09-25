# Sets in python.
# Sets is a collection of non-repetitive objects.

# s = {} # empty dictionary.
# a = set() # empty set.

s = {1, 2, 3,3,3,3} # set.
print(s) # it will print 3 only one time, it doesnot take repeated value.

s2 = {1, 2, 3, "3", 3.0} # it will treat int and float same but string "3" like other value. it will print 1, 2, 3, '3' only not 3.0 because 3 is already there.
print(s2) # 3 == 3.0 because the value is same.