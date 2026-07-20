# 1.Create a Python package folder named 'musicplayer' with 
# an __init__.py file inside it, then add a simple function play_song() 
# in a new file player.py within the package that prints 'Playing song...'. 
# Import and call play_song() from a separate script outside the package.

# player.py
def play_song():
    print("Playing song...")
# __init__.py
# from .player import play_song
# main.py
# from musicplayer import play_song
play_song()

# 2.Inside a package folder called 'foodorder', create two modules: menu.py 
# (with a function get_menu() returning a list of food items) and order.py 
# (with a function place_order(item) that prints 'Order placed for: item'). 
# Use __init__.py to import both functions so they can be accessed directly 
# from the package.<br><br><em><strong>Hint:</strong> Use 'from .menu import 
# get_menu' and 'from .order import place_order' in __init__.py.</em>

def get_menu():
    return ["Pizza", "Burger", "Pasta", "Sandwich", "Dosa"]
def place_order(item):
    print("Enter your order = ", item)

menu = get_menu()
print("Food Menu")
for i in menu:
    print(i)

item = input("Enter your food item = ")

if item in menu:
    place_order(item)
else:
    print("Not Available !!!")

# 3.Refactor an existing 'shoppingcart' package by moving the add_to_cart() 
# function from cart.py to a new module actions.py, updating __init__.py to 
# reflect the change so that add_to_cart() is still accessible from the package 
# import.<br><br><em><strong>Constraint:</strong> Do not change the function's 
# definition or logic, only its location and the import paths.</em>

def add_to_cart(item, cart):
    cart.append(item)
    return cart

cart = []

item = input("Enter Product Name: ")

add_to_cart(item, cart)

print("Shopping Cart:", cart)

# 4.Build a package named 'instahelpers' with an __init__.py file that exposes a 
# function format_likes(count) which returns '1.2K' for 1200, '1.5M' for 1500000, 
# or the actual number for less than 1000, similar to Instagram's like counter. 
# Write a script to test this with various counts.

def format_likes(count):

    if count >= 1000000:
        return str(round(count / 1000000, 1)) + "M"

    elif count >= 1000:
        return str(round(count / 1000, 1)) + "K"

    else:
        return str(count)


likes = [950, 1200, 45000, 1500000]

for i in likes:
    print(i, "->", format_likes(i))

# 5.Use ChatGPT or Copilot to generate boilerplate code for a Python package named 
# 'ticketbooking' with an __init__.py, a search.py module (with a search_event() function), 
# and a booking.py module (with a book_ticket() function). Then, manually add a print 
# statement to each function to confirm they work when imported.

def search_event():
    print("Searching Event...")

def book_ticket():
    print("Ticket Booked Successfully...")

search_event()
book_ticket()