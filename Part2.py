import re 

email = input("What's your email? ").strip() 

if re.search(r".+@.+\.ac.uk", email):
    print("Valid")
else: 
    print("Invalid")

#introducing re
#. any character except a new line
#* 0 or more repetitions
#+ 1 or more repetitions
#? 0 or 1 repetition
#{m} m repetitions
#{m,n} m-n repetitions