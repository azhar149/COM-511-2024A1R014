# write a program to reverse every kth row in a matrix
def reverse_kth_row(matrix, k):
    for i in range(len(matrix)):
        if (i + 1) % k == 0:
            matrix[i] = matrix[i][::-1]
    return matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
k = int(input("Enter row to reverse: "))
result = reverse_kth_row(matrix, k)
for row in result:
    print(row)