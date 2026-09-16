"""
WAP to print a square pattern of stars for n rows and m columns.
"""

n = int(input("Enter rows length : "))
m = int(input("Enter columns length : "))

for i in range(n):
    for j in range(m):
        print("*", end = " ")
    print()