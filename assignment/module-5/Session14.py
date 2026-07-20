# 1.Create a dynamic nested dictionary in Python to represent a Flipkart 
# shopping cart where each user (by username) can have multiple items, and each 
# item has a name, quantity, and price. Add two users with at least two items each, 
# then print the entire cart.

cart = {}

for i in range(2):
    username = input("Enter Username: ")

    cart[username] = {}

    for j in range(2):
        item = input("Enter Item Name: ")
        quantity = int(input("Enter Quantity: "))
        price = int(input("Enter Price: "))

        cart[username][item] = {
            "Quantity": quantity,
            "Price": price
        }

print("\nShopping Cart")

for user in cart:
    print("\nUser:", user)

    for item in cart[user]:
        print("Item:", item)
        print("Quantity:", cart[user][item]["Quantity"])
        print("Price:", cart[user][item]["Price"])

# 2.Write a function add_song_to_playlist(playlists, user, playlist_name, song_title, artist) 
# that adds a song to a user's playlist in a nested dictionary structure like Spotify. 
# If the user or playlist doesn't exist, create them dynamically.

def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):

    if user not in playlists:
        playlists[user] = {}

    if playlist_name not in playlists[user]:
        playlists[user][playlist_name] = []

    playlists[user][playlist_name].append({
        "Song": song_title,
        "Artist": artist
    })


playlists = {}

user = input("Enter User Name: ")
playlist = input("Enter Playlist Name: ")
song = input("Enter Song Name: ")
artist = input("Enter Artist Name: ")

add_song_to_playlist(playlists, user, playlist, song, artist)

print("\nPlaylists")
print(playlists)

# 3.Build a dynamic nested dictionary to store IPL cricket match scores: for each team, 
# store a dictionary of player names and their runs. Add at least two teams with three 
# players each, then print the runs scored by a specific player of your choice.

scores = {}

for i in range(2):
    team = input("Enter Team Name: ")

    scores[team] = {}

    for j in range(3):
        player = input("Enter Player Name: ")
        runs = int(input("Enter Runs: "))

        scores[team][player] = runs

print("\nIPL Scores")
print(scores)

team = input("\nEnter Team Name to Search: ")
player = input("Enter Player Name to Search: ")

print("Runs Scored:", scores[team][player])

# 4.Given a nested dictionary representing Zomato orders (order_id as key, value is another 
# dictionary with 'restaurant', 'items' (list), and 'total'), write a function to add a new 
# order and another function to update the total of an existing order.<br><br><em><strong>Hint:
# </strong> Use dict.setdefault() to handle missing keys dynamically.</em>

orders = {}

def add_order(order_id, restaurant, items, total):
    orders.setdefault(order_id, {})
    orders[order_id]["Restaurant"] = restaurant
    orders[order_id]["Items"] = items
    orders[order_id]["Total"] = total

def update_total(order_id, new_total):
    if order_id in orders:
        orders[order_id]["Total"] = new_total

order_id = int(input("Enter Order ID: "))
restaurant = input("Enter Restaurant: ")
items = input("Enter Items (comma separated): ").split(",")
total = int(input("Enter Total: "))

add_order(order_id, restaurant, items, total)

new_total = int(input("Enter New Total: "))
update_total(order_id, new_total)

print(orders)

# 5.Refactor the following code to use dynamic nested dictionary creation so that 
# it doesn't throw a KeyError when adding a new user or playlist:<br><br>playlists = 
# {'user1': {'Favourites': ['Song1', 'Song2']}}<br>playlists['user2']['Chill'].append('Song3')
# <br><br><em><strong>Hint:</strong> Use collections.defaultdict or check if keys exist 
# before accessing.</em>

from collections import defaultdict

# Create nested defaultdict
playlists = defaultdict(lambda: defaultdict(list))

# Existing data
playlists['user1']['Favourites'] = ['Song1', 'Song2']

# Add new user and playlist automatically
playlists['user2']['Chill'].append('Song3')

print(dict(playlists))
