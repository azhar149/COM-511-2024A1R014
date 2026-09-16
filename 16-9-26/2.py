# wapp to input marks of 10 students.store only valid marks between 0 and 100 in a list.skip invalid marks.
marks = []
for i in range(10):
    mark = int(input(f"Enter marks for student {i+1}: "))
    if 0 <= mark <= 100:
        marks.append(mark)
    else:
        print("Invalid mark. Please enter a value between 0 and 100.")
print(f"Valid marks: {marks}")