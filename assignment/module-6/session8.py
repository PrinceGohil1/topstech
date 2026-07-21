#1 Create a Python script called insta_caption.py 
# that takes a user's Instagram caption as input and prints 
# the first 10 characters using string indexing.

caption = input("Enter your Instagram caption: ")

print("First 10 characters:", caption[:10])

#2 Write a function extract_artist(song_title) that takes a 
# string in the format 'Song Name - Artist Name' 
# (like you see on Spotify) and returns just the artist's 
# name using string slicing.<br><br><em><strong>Hint:
# </strong> Use the index() method to find the position of 
# the dash.</em>

def extract_artist(song_title):
    dash_position = song_title.index("-")
    artist = song_title[dash_position + 2:]   # Skip "- "
    return artist

song = "Believer - Imagine Dragons"
print("Artist:", extract_artist(song))

#3 Build a function reverse_message(message) that reverses 
# any string passed to it, similar to how WhatsApp displays 
# reversed text stickers.<br><br><em><strong>Constraint:
# </strong> Do not use Python's built-in reversed() or 
# [::-1] slicing shortcut.</em>

def reverse_message(message):
    reversed_text = ""
    index = len(message) - 1

    while index >= 0:
        reversed_text += message[index]
        index -= 1

    return reversed_text

msg = input("Enter a message: ")
print("Reversed message:", reverse_message(msg))

#4 Given a Flipkart product description string, write a Python 
# script that extracts and prints the first word, last word, 
# and the total number of words using string methods split(),
# indexing, and len().

description = input("Enter the Flipkart product description: ")

words = description.split()

if len(words) > 0:
    print("First word:", words[0])
    print("Last word:", words[-1])
    print("Total number of words:", len(words))
else:
    print("No description entered.")


#5 Create a function mask_phone_number(phone) that takes a 
# 10-digit phone number as a string and returns it in the 
# format '******1234', showing only the last 4 digits like 
# Paytm does.<br><br><em><strong>Hint:</strong> Use string 
# slicing and concatenation.</em>

def mask_phone_number(phone):
    return "******" + phone[-4:]

phone = input("Enter a 10-digit phone number: ")
print("Masked Phone Number:", mask_phone_number(phone))