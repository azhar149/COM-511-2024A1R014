correct_username=input("Enter Correct_Username:")
correct_password=input("Enter Correct_Password:")
attempts=3
while attempts>0:
    username=input("Enter Username:")
    password=input("Enter Password:")

    if username==correct_username and password==correct_password:
        print("Login Successful")
        break
    else:
        attempts=attempts-1
        print("Worng details.Attempts left:",attempts)

    if attempts==0:
        print("Account Locked")