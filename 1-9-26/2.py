# WAP to fill the given letter template with name and date.
# letter ='''
# Dear <Name>,
# You are Selected!
# <Date>
# '''

letter ='''
Dear <Name>,
You are Selected!
<Date>
'''

name = input("Enter Name : ")
date = input("Enter Date : ")

letter = letter.replace("<Name>", name)
letter = letter.replace("<Date>", date)

print(letter)


# from datetime import date

# name = input("Enter a Name : ")
# # date = date.today()
# date = "1st September, 2026" 

# print(f'''
# Dear {name},
# You are Selected!
# {date}
# ''')