"""
WAP to input a student's marks in n consecutive tests and store them in a list.
Find the longest consecutive sequence in which each mark is strictly greater than the previous mark.

Display the sequence, its length, and starting and ending test numbers as a tuple.
If multiple sequences have the same maximum length, display the first one.

Marks: [55,60,68,62,65,70,78,74]
Longest improving sequence: [62,65,70,78]
Number of tests: 4
Test range: (4, 7)

Conditions:
> Accept at least one test.
> Equal marks break the improving sequence.
> Test numbers begin at 1.
> Do not sort the list because the original test orders matters.
"""


n = int(input("Enter number of tests: ")) 
while n < 1:
    print("Please enter at least one test.") 
    n = int(input("Enter number of tests: ")) 
    
marks = list(map(int, input("Enter marks: ").split())) 

start = 0 
end = 0 
current_start = 0
for i in range(1, n):
    if marks[i] > marks[i - 1]: 
        if i - current_start > end - start: 
            start = current_start 
            end = i 
    else: 
        current_start = i 

sequence = marks[start:end + 1] 
length = end - start + 1 

print("Marks:", marks) 
print("Longest improving sequence:", sequence) 
print("Number of tests:", length) 
print("Test range:", (start + 1, end + 1))