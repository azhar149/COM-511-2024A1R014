# WAP to take input from user without typecasting and multiply it by 3.
# Then typecast the same input to int and multiply it by 3. Print both results to show the difference

num = input("Enter a number : ")

res1 = num * 3
print("Without Typecasting : ",res1)

num = int(num)
res2 = num * 3
print("After Typecasting : ",res2)