import re

phone = input("What is your phone number?")

if re.search(r"^07\d{9}$", phone): 
    print("Valid")
else: 
    print("Invalid")