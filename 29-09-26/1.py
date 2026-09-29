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

