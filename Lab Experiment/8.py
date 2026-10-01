# Create a dictionary using lists and tuples.Each student record must contain roll number,name,ranch and CGPA. Store each record as a  tuple inside a list.Display all records and search for a student using roll number.
# conditions:
# 1. Each record should be stored as a tuple.
# 2. The complete databaseshould be stored as a list.
# 3. Roll numbers must be unique.

n = int(input("Enter number of students: "))
database = []
for i in range(n):
    roll_no=int(input("Enter roll number: "))
    name=input("Enter name: ")
    branch=input("Enter branch: ")
    cgpa=float(input("Enter CGPA: "))
    student_record = (roll_no, name, branch, cgpa)
    database.append(student_record)
print("\nStudent Database:")
for student in database:
    print(student)
search_roll = int(input("\nEnter roll number to search: "))
found = False
for student in database:
    if student[0] == search_roll:
        print("\nStudent Record Found")
        print("Roll Number:", student[0])
        print("Name:", student[1])
        print("Branch:", student[2])
        print("CGPA:", student[3])
        found = True
        break

if not found  :
    print("Student record not found.")