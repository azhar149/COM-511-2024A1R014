# WAP to take a student name and roll number,
# then generate a username using the first 3 letters of the name and last 2 digits of the roll number

name = input("Enter Name : ")
rollno = input("Enter Roll no : ")

username = name[0:3] + rollno[-2:]

print("Username : ",username)

# print("username :", name[0:3] + rollno[-2:])