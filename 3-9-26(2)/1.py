# WAP to determine whether a student is eligible for a scholarship.
# The scholarship should be granted if the student satifies either of the following conditions:
# a) The student has a CGPA of 8.5 or above and attendence of 85 percent or above
# b) The student has won a national-level compition

# The program should take CGPA, attendence percentage and national-level competition status as input, 
# then display whether the student is eligible for the scholarship

CGPA = float(input("Enter CGPA : "))
attendance = int(input("Enter attendence : "))
is_eligible = input("Have you won a national-level competition? yes/no : ")

if (CGPA >= 8.5 and attendance >= 85) or is_eligible == "yes":
    print("Student is eligible for Scholarship.")
else:
    print("Student is not eligible for Scholarship.")