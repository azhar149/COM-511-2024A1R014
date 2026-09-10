#wapp to take a decimal number as input and convert it into binary without using bin() function.
n=float(input("Enter a decimal number: "))
binary=""
while n>0:
    binary=str(n%2)+binary
    n//=2
print("Binary equivalent:", binary)