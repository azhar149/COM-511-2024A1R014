# write a python program to input marks of n students ina a list dispaly highest marks and lowest marks ,average and number fo students who passed
n = int(input("Enter the number of students: "))
marks = []
for i in range(n):
    mark = int(input(f"Enter marks for student {i+1}: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)
passed = len([mark for mark in marks if mark >= 40])

print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")
print(f"Average marks: {average}")
print(f"Number of students who passed: {passed}")