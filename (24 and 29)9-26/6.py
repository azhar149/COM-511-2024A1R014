"""
WAP to store one student data as a tuple: name, roll number, and marks.
Display grade based on marks.
"""

name = input("Enter a Name : ")
rollno = int(input("Enter Roll Number : "))
marks = int(input("Enter Marks : "))

stu = (name, rollno, marks)

print(stu)

grade = ""

if 75 <= marks <= 100:
    grade = 'A'
elif 61 <= marks <= 74:
    grade = 'B'
elif 51 <= marks <= 60:
    grade = 'C'
elif 40 <= marks <= 50:
    grade = 'D'
else:
    grade = 'F'

print("Name :",stu[0])
print("Roll Number :",stu[1])
print("Marks :",stu[1])
print("Grade :",grade)