# write a python program to create records of n students.Store each student record as a dictionary containing roll number, name,branch and cgpa.store each record as a tuple inside a list.Display all records and search for a student using roll number.
n = int(input("Enter number of students: "))
students = []

for _ in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA: "))
    student = (roll, name, branch, cgpa)
    students.append(student)

print("All Student Records:")
for student in students:
    print(f"Roll: {student[0]}, Name: {student[1]}, Branch: {student[2]}, CGPA: {student[3]}")

search_roll = int(input("Enter roll number to search: "))
found = False
for student in students:
    if student[0] == search_roll:
        print(f"Student found - Roll: {student[0]}, Name: {student[1]}, Branch: {student[2]}, CGPA: {student[3]}")
        found = True
        break

if not found:
    print("Student not found.")