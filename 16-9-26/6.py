# wap to rotate a list one position to right
numbers = [1, 2, 3, 4, 5]
numbers = [numbers[-1]] + numbers[:-1]
print(f"Rotated list: {numbers}")