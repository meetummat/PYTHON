# Write a program to find out whether a given post is talking about “Meet” or not.

post = input("Enter post : ")

# at the time of comparison "Meet" and post will be converted into lowercase.
if "Meet".lower() in post.lower(): # now if anyone enter name in lower or upper or any letter in lower or uppercase then it will also detect that.
    print("This post is talking about Meet")
else:
    print("This post is not talking about Meet")

# or we can compare as
# if "meet" in post.lower()