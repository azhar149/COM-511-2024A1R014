# Write a Python program to input marks of 5 students.
# For each student, the program should check whether the entered marks are valid or invalid. Marks are considered valid only if they are between 0 and 100. If the marks are considered valid only if they are betwwen 0 and 100. If the marks are invalid, the program should display "Invalid marks skipped " and move to the next student without printing those marks. if the marks are valid, the program should display the marks as valid.


for i in range(1,6):
    marks = float(input("Enter marks: "))

    if 0 <= marks <= 100:
        print("Valid marks:", marks)
    else:
        print("Invalid marks skipped")