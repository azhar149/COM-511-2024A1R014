# Write a Python program to create a simple password validation system.
# The should repeatedly ask the user to enter a password until a valid password is enetered. A password will be considered valid only if it has at 8 characters and contains the @ symbol.
# Once the user enetrs a valid password, the program should display"Password accepted". and stop. Otherwise, it should display"Weak password. Try again." and ask for the password again.


p = input("Enter password: ")

if len(p) >= 8 and "@" in p:
    print("Password accepted")
else:
    print("Weak password. Try again.")
