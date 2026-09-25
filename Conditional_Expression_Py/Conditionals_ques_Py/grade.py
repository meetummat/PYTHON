# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter your marks : "))

if marks < 0 or marks > 100:
    print("Please enter valid marks")

elif marks >= 90:
    print("Excellent")

elif marks >= 80:
    print("A Grade")

elif marks >= 70:
    print("B Grade")

elif marks >= 60:
    print("C Grade")

elif marks >= 50:
    print("D Grade")

else:
    print("Fail")
