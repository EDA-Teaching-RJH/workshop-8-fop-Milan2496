import re 

email = input("What's your email? ").strip() 

if re.search(r"^\w+@\w.+\.(ac.uk | gov.uk | nhs.net)$", email): 
    print("Valid")
else: 
    print("Invalid")


#\d decimal digit
#\D not a decimal digit
#\s whitespace characters
#\S not a whitespace character
#\w word character, as well as numbers and the underscore
#\W not a word character