# Wapp to input 4 no from the user and find the greatest number among them
a=int(input("Enter first number :- "))
b=int(input("Enter second number :- "))
c=int(input("Enter third number :- "))
d=int(input("Enter fourth number :- "))


if a>b and a>c and a>d:
    print("Greatest number is :- ",a)
elif b>a and b>c and b>d:
    print("Greatest number is :- ",b)
elif c>a and c>b and c>d:
    print("Greatest number is :- ",c)
else:
    print("Greatest number is :- ",d)