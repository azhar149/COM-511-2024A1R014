# Take an email address and print username, domain, and reversed domain.

email = input("Enter an Email : ")

at_pos = email.find("@")

username = email[:at_pos]
domain = email[at_pos + 1:]
rev_domain = domain[::-1]

print("Username :",username)
print("Domain :",domain)
print("Reversed Domain :",rev_domain)

# username = email.split("@")[0]
# print("Username :",username)

# domain = email.split("@")[1]
# print("Domain :",domain)

# print("Reversed Domain :",domain[::-1])