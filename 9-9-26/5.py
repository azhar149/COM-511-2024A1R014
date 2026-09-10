#2. Write a Python program to input a number and check whether it is prime or not.
# A number is prime if it has no divisor other than 1 and itself.
number=int(input("Enter Number:"))
if number%2!=0:
    print("Prime Number")
else:
    print("Not Prime Number:")