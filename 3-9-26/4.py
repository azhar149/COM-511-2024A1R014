# Take name, branch and year. Generate a code name using string concatenation, slicing, and repetation.

name = input("Enter a Name : ")
branch = input("Enter Branch Name : ")
year = input("Enter Year : ")

code_name = name[:3] + "-" + branch[:3] + "-" + year[-2:]

print("*" * 30)
print("Student Code :",code_name)
print("*" * 30)