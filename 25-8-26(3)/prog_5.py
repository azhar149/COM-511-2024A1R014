# WAP to take student details like name, roll no, cgpa, and hostel satus from the user.
# Typecast them into appropirate types and print them along with their detected type.

name = input("Enter Student Name")
roll_no = int(input("Enter roll number: "))
cgpa = float(input("Enter CGPA: "))
is_hosteller = bool(input("Are you a hosteller: "))


print("Name:", name, type(name))
print("Roll No:", roll_no, type(roll_no))
print("CGPA:", cgpa, type(cgpa))
print("Hostel Status:", is_hosteller, type(is_hosteller))