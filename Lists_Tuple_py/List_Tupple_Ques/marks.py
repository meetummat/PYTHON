# accept marks of student and display in sorted mannar.

marks = []

eng_marks = int(input("Enter marks of English : "))
marks.append(eng_marks)
hindi_marks = int(input("Enter marks of Hindi : "))
marks.append(hindi_marks)
maths_marks = int(input("Enter marks of Maths : "))
marks.append(maths_marks)
sci_marks = int(input("Enter marks of Science : "))
marks.append(sci_marks)
sst_marks = int(input("Enter marks of Social Studies : "))
marks.append(sst_marks)

marks.sort() # will perfect sort when its of string type

print(marks)