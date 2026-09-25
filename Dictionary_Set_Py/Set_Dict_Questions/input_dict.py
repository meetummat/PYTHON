# Create an empty dict. Allow 4 friends to enter their favourite language as value.

d = {}

name = input("Enter you name : ")
lang = input("Enter language name : ")
d.update({name: lang})

name = input("Enter you name : ")
lang = input("Enter language name : ")
d.update({name: lang})

name = input("Enter you name : ")
lang = input("Enter language name : ")
d.update({name: lang})

name = input("Enter you name : ")
lang = input("Enter language name : ")
d.update({name: lang}) 
# If two friends have same name then it will update the name with the language we wrote at the end.
# if the value of two friends are same then it will not make any impact on out program.

print(d)