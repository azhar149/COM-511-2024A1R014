# Take student full name and roll number. Generate email using first 3 letters of first name, 
# first 3 letters of last name, and last 3 characters of roll numbers.

full_name = input("Enter Full Name : ")
rollno = input("Enter Roll No. : ")

space_idx = full_name.find(" ")

fname = full_name[:space_idx]
lname = full_name[space_idx + 1:]

email = fname[0:3] + lname[0:3] + rollno[-3:] + "@mietjammu.in"
print("Email :",email)


# fname = input("Enter First Name : ")
# lname = input("Enter Last Name : ")
# rollno = input("Enter Roll No. : ")

# email = fname[0:3] + lname[0:3] + rollno[-3:] + "@mietjammu.in"
# print("Email :",email)

# print(f"Email : {fname[0:3]}{lname[0:3]}{rollno[-3:]}")