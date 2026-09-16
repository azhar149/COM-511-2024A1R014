"""
WAP to print an inverted right-angled triangle using stars.
* * * *
* * *
* *
*
"""

n = int(input("Enter val of N : "))

for i in range(n):
    for j in range(n - i):
        print("*", end = " ")
    print()