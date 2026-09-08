# WAP to take two inputs a and b, seap their values using a temperary variable and print updated values

a = int(input("Enter value of 'a' : "))
b = int(input("Enter value of 'b' : "))

t = a
a = b
b = t

# a, b = b, a 

print("After swapping : ",a ,b)