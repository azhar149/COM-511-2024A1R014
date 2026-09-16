"""
WAP to print the following pattern for n rows:
1
1 2
1 2 3
1 2 3 4
"""
n = int(input("Enter value of N : "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()