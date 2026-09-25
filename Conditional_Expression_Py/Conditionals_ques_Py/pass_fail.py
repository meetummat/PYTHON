# whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

hindi_marks = int(input("Enter marks of Hindi : "))
eng_marks = int(input("Enter english marks : "))
sci_marks = int(input("Enter science marks : "))
# total_percentage = ((hindi_marks + eng_marks + sci_marks) * 100)/300
total_percentage = (hindi_marks + eng_marks + sci_marks)/3

if (total_percentage < 40 or hindi_marks < 33 or eng_marks < 33 or sci_marks < 33):
    print(f"Failed {total_percentage:.2f}%")
else:
    print(f"Pass {total_percentage:.2f}%") # it will print only 2 values after decimal point.