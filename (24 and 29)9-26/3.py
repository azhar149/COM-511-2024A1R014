"""
WAP to show that tuple values cannot be changed directly.
Convert tuple into list, update it, and convert it back into tuple.
"""

tup = (10, 20, 30, 67, 69)

print("Tuple :- ",tup)

# tup[0] = 50
# Gives Error

lst = list(tup)
lst[1] = 50
print("Converted Tuple :-",list(tup))


print("Updated Tuple :-",tuple(lst))