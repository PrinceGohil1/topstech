# 1.Use the math.sqrt() function to calculate and print 
# the square roots of the numbers 16, 49, and 81.

import math
print(math.sqrt(16))
print(math.sqrt(49))
print(math.sqrt(81))

# 2.Build a Flipkart-style price rounder: given a list of product 
# prices with decimals, use math.ceil() to round each price up to 
# the nearest whole number and display the results.<br><br><em><strong>Hint:
# </strong> Try with prices like 199.1, 349.8, and 599.3.</em>

import math
prices = [199.1, 349.8, 599.3]
for i in prices:
    print(math.ceil(i))

# 3.Create a Zomato order bill calculator that uses math.floor() to show 
# the final bill amount after applying a 10% discount, rounding down to the nearest rupee.

import math
bill = 1250
discount = bill * 10 / 100
ans= bill - discount

print(f"{"Final Bill = "}{math.floor(ans)}")

# 4.Simulate a dice roll for a board game app using random.randint(1, 6) 
# and print the result each time you run the program.

import random
ans=random.randint(1, 6)
print(f"The number is {ans}")

# 5.Build a Spotify-style daily playlist shuffle: given a list of 8 song names, 
# use the random module to select and print 3 random songs for today's playlist.
# <br><br><em><strong>Hint:</strong> Use random.sample() for this task.</em>

import random

songs = ["Kesariya","Believer","Shape of You","Perfect",
         "Levitating","Apna Bana Le","Closer","Blinding Lights"]

playlist = random.sample(songs, 3)

print("Today Playlist = ")
for song in playlist:
    print(song)
