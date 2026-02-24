import re 

email = input("What's your email? ").strip() 

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.ac.uk$", email): 
    print("Valid")
else: 
    print("Invalid")

#^ matches the start of the string
#$ matches the end of the string or just before the newline at the end of the string
#We can use [^@] to match anything except an @.