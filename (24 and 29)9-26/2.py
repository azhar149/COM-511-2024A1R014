"""
WAP to store all month names in a tuple. Input a month number and display the crossponding month name. 
"""

months = ("January", "Feburary", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

num = int(input("Enter Month Number : "))

if 1 <= num <= 12:
    print("Month : ",months[num - 1])
else:
    print("Invalid Month Number")