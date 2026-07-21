#1 Create a dictionary called my_playlist with three songs as keys and their durations in minutes as values, then print the dictionary.

my_playlist = {
    "Shape of You": 4.2,
    "Blinding Lights": 3.3,
    "Kesariya": 4.5
}

print("My Playlist:", my_playlist)

#2 Add a new song and its duration to your my_playlist 
# dictionary, then update the duration of one existing song.

my_playlist = {
    "Shape of You": 4.2,
    "Blinding Lights": 3.3,
    "Kesariya": 4.5
}

my_playlist["Perfect"] = 4.4

my_playlist["Kesariya"] = 4.7

print("Updated Playlist:", my_playlist)

#3 Write a function display_friends() that takes a 
# dictionary of Instagram usernames as keys and their 
# follower counts as values, and prints each username with 
# their followers in the format: 'username: 2.3K followers'.

def display_friends(friends):
    for username, followers in friends.items():
        print(f"{username}: {followers/1000:.1f}K followers")


instagram_friends = {
    "umang_07": 2300,
    "rahul_99": 1850,
    "priya_official": 4200,
    "meet_patel": 3150
}

display_friends(instagram_friends)

#4 Given a dictionary called food_order = {'Pizza': 2, 
# 'Burger': 1, 'Fries': 3}, use the keys(), values(), and 
# items() methods to print: a) all food items, b) all 
# quantities, and c) each item with its quantity.

food_order = {
    "Pizza": 2,
    "Burger": 1,
    "Fries": 3
}

print("Food Items:")
print(food_order.keys())

print("\nQuantities:")
print(food_order.values())

print("\nItem and Quantity:")
for item, quantity in food_order.items():
    print(f"{item}: {quantity}")

#5 Build a function update_cart(cart, item, qty) that adds 
# a new item to a Flipkart-style cart dictionary or updates 
# the quantity if the item already exists, then returns 
# the updated cart.<br><br><em><strong>Hint:</strong> Use 
# the dictionary's update() method or direct assignment 
# for adding/updating entries.</em>

def update_cart(cart, item, qty):
    cart[item] = qty      # Adds a new item or updates the existing item's quantity
    return cart

cart = {
    "Laptop": 1,
    "Mouse": 2,
    "Keyboard": 1
}

update_cart(cart, "Headphones", 1)
print("After adding a new item:")
print(cart)

update_cart(cart, "Mouse", 3)
print("\nAfter updating an existing item:")
print(cart)