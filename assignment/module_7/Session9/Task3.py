#Create a function extract_hashtags(text) that uses re.findall() to return all hashtags (words starting with #) from a given Instagram-style caption string.

import re

def extract_hashtags(text):
    return re.findall(r"#\w+", text)

text="Learning Python #Python #Coding #AI"
ans=extract_hashtags(text)
print(ans)