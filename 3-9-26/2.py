# Take roll number like 2024A1R036 and extract admission year, program code, and roll number digits using slicing

rollno = input("Enter a Roll Number")

print("Admission Year :",rollno[0:4])
print("Program Code :",rollno[4:6])
print("Roll Digits :",rollno[-3:])