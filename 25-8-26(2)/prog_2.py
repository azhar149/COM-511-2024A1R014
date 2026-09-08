# WAP to swap tw0 numbers without using a third variable (use arithmatic opeators)

a = int(input("Enter value of 'a' : "))
b = int(input("Enter value of 'b' : "))

a = a + b
b = a - b
a = a - b

# a, b = b, a 

print("After swapping : ",a ,b)