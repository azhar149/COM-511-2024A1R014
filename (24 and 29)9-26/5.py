"""
WAP to check whether a given value is present in a tuple.
If present, display its position.
"""

tup = (10, 20, 30, 40, 50, 60, 70, 80, 90)

val = int(input("Enter a value to check in Tuple : "))

if val in tup:
    print("Value is present.")
    print("Position : ",tup.index(val))
else:
    print("Value not Found in Tuple.")

# for i in range(len(tup)):
#     if tup[i] == val:
#         print("Value is at Position",i)