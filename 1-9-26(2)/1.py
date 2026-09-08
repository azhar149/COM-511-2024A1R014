# WAP to take a student's full name and display:
# -> Total number of characters
# -> First character
# -> Last Character
# -> Name in uppercase form 

name = input("Enter Full Name : ")

print("Total number of characters :",len(name))
print("First character :",name[0])
print("Last character :",name[-1])
print("Name in Uppercase form :",name.upper())