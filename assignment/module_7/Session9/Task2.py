#Use re.search() to find and print the first 10-digit mobile number in a string that contains a mix of text and phone numbers, similar to how Zomato or Swiggy might display contact info in reviews.

import re

text = "My number 6353300654"
find = re.search(r"\d{10}", text)

print(find.group())