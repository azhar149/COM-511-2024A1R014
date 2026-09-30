# Write a Python program to inputs student's marks in consecutive tests and store them a list. Find the longest consecutive sequence in which each markist mark
# Display the sequence, its length, and its starting and ending test runten ten sequences have the same maximum length, display the first the
# Marks: (55, 60, 68, 62, 65, 70, 78, 741
# Longest improving sequence: (62, 65, 70, 78)
# Number of tests: 4
# Test range: (4, 7)

     # Conditions:
# Accept at least one test.
# Equal marks break the improving sequence
# Test numbers begin at 1.
# Do not sort the list because the original test order matters

marks = [55, 60, 68, 62, 65, 70, 78, 74]
longest = [marks[0]]
current = [marks[0]]
start = 1
longest_start = 1
for i in range(1, len(marks)):
    if marks[i] > marks[i - 1]:
        current.append(marks[i])
    else:
        current = [marks[i]]
        start = i + 1

    if len(current) > len(longest):
        longest = current
        longest_start = start

longest_end = longest_start + len(longest) - 1
print("Marks:", marks)
print("Longest improving sequence:", longest)
print("Number of tests:", len(longest))
print("Test range:", (longest_start, longest_end))