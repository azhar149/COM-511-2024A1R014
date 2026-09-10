# wapp to detect whether a no is spam or not.
# A comment should be treated as a spam if it contain any of these keywords :
# "make a lot money","buy now ","subscribe this ",or click this "."

comment=input("Enter comment : ")
comment = comment.lower()
if "make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment or "click this" in comment:
    print("This comment is spam")
else:
    print("This is not a spam comment.")