# wapp to create a list of numbers and create a new list contaning only unique elements
numbers = [1, 2, 3, 2, 4, 1, 5]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print(unique)
