#Use ChatGPT to generate a regular expression that matches Indian Railways PNR numbers (10-digit numbers), then implement a Python function is_valid_pnr(pnr) using re.match() to validate user input. Paste the regex and your function in your submission.

import re

def is_valid_pnr(pnr):
    pattern=r"^\d{10}$"

    if re.match(pattern,pnr):
        return True
    else:
        return False

pnr = input("Enter PNR Number = ")

if is_valid_pnr(pnr):
    print("This is Valid PNR")
else:
    print("This is Invalid PNR")