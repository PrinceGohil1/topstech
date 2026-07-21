#1 Create a tuple called fav_apps containing the names of 
# your 5 most-used mobile apps (for example: 'Instagram', 
# 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart') and print the tuple.

fav_apps = ("Instagram", "WhatsApp", "Spotify", "YouTube", "ChatGPT")

print("My Favorite Apps:", fav_apps)

#2 Access and print the 2nd and 4th app names from your 
# fav_apps tuple using indexing.

fav_apps = ("Instagram", "WhatsApp", "Spotify", "YouTube", "ChatGPT")

print("2nd App:", fav_apps[1])
print("4th App:", fav_apps[3])

#3 Try to change the first element of your fav_apps tuple to 'YouTube' and observe the error message. Write a comment explaining why this happens based on tuple immutability.

fav_apps = ("Instagram", "WhatsApp", "Spotify", "YouTube", "ChatGPT")

fav_apps[0] = "YouTube"

print(fav_apps)

#4 Use tuple slicing to print the middle three app names 
# from your fav_apps tuple.<br><br><em><strong>Hint:
# </strong> Use tuple[start:end] syntax to select a range 
# of elements.</em>

fav_apps = ("Instagram", "WhatsApp", "Spotify", "YouTube", "ChatGPT")

print("Middle Three Apps:", fav_apps[1:4])

#5 Create another tuple called new_apps with two more app names you want to try. Concatenate fav_apps and new_apps into a single tuple called all_apps and print the result.

fav_apps = ("Instagram", "WhatsApp", "Spotify", "YouTube", "ChatGPT")

new_apps = ("Netflix", "Threads")

all_apps = fav_apps + new_apps

print("All Apps:", all_apps)