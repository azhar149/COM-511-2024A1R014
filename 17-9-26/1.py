"""
WAP to store two points as tuples and calculate the distance between them.
"""
x1 = int(input("Enter x1 : "))
y1 = int(input("Enter y1 : "))
x2 = int(input("Enter x2 : "))
y2 = int(input("Enter y2 : "))

p1 = (x1, y1)
p2 = (x2, y2)

distance = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
print(f"The distance between the points is: {distance}")