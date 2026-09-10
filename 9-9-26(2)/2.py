# write a python program to input a two number and find their greatet common divisor using loop
a=int(input("enter first numer : "))
b=int(input("enter second number : "))
num1,num2=a,b
while b!=a:
    remainder = a % b
    a = b
    b= remainder
print(f"the gcd of {num1} and {num2} is {a}")