# WAP to take marks of 3 subjects out of 100.
# Print true if the student scored at least 40 in all three subjects and avg marks are at least 50

m1 = int(input("Enter Subject 1 Marks : "))
m2 = int(input("Enter Subject 2 Marks : "))
m3 = int(input("Enter Subject 3 Marks : "))

avg = (m1 + m2 + m3) / 3

print(m1 >= 40 and m2 >= 40 and m3 >= 40 and avg >= 50)