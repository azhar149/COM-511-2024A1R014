# WAP to take total minutes as input and convert it into hours and remaining minutes

min = int(input("Enter Minutes : "))

hrs = min // 60
minutes = min % 60 # min - (hrs * 60)

print(f"{hrs} Hours and {minutes} minutes")