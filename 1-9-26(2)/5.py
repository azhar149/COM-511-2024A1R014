# WAP to take 10-digit mobile number and display only the last 4 digits. 
# Replace the first 6 digits with ******

num = input("Enter a 10-digit Mobile Number : ")

masked = "******" + num[-4:]

print("Masked mobile Number =", masked)

# masked = number.replace(number[0:6],"******")

# print(masked)