# WAP to take an amount in rupees and calculate how many 500 and 100 notes are needed

amt = int(input("Enter an Amount : "))

note_500 = amt // 500
rem_amt = amt % 500
note_100 = rem_amt // 100

print(f"{note_500} Notes of 500 & {note_100} Notes of 100")