# WAP to take a 2-digit number as input and print the sum of its digits

n = int(input("Enter a 2-digit number : "))

first = n // 10
sec = n % 10

print(f"Sum of 2-digits numbers : {first + sec}")

# x = n % 10
# num = x
# num = n // 10

# print(f"{x + num}")