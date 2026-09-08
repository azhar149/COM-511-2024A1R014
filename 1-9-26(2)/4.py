# WAP to take an email address and print the domain name

email = input("Enter an Email : ")

index = email.find("@")
domain = email[index + 1:]

print("Domain :",domain)

# domain = email.split("@")[1]

# print("Domain Name :",domain)