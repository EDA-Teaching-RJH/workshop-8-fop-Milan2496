import re

phone = input("What is your phone number?")

if re.search(r"^[A-Za-z]{4}[0-9]{4}$", phone): 
    print("Valid")
else: 
    print("Invalid")