"""
WAP to print a centered pyramid using stars.
      *

    * * *

  * * * * *

* * * * * * *
"""

n =  int(input("Enter value of N : "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = " ")
    for j in range(2 * i + 1):
        print("*", end = " ")
    print()