# Build a menu-management tool that uses dictionaries, list comprehension, and the random
# module to categorise and filter a restaurant's offerings.
# Store the menu as a dictionary where each key is an item name and the value is a nested dict
# with 'price' (int) and 'category' (str, e.g. 'Starter', 'Main', 'Dessert').
# Use list comprehension to produce a filtered list of item names whose price is below a
# user-entered budget; print this 'Budget Picks' list.
# Import the random module and use random.choice() to suggest one random item as the
# 'Chef's Pick of the Day'.
# Group items by category using a loop and display each group with item names and the
# average price of that category rounded to 2 decimal places.
import random


# Restaurant Menu
menu = {
    "pizza": {
        "price": 500,
        "category": "main"
    },

    "burger": {
        "price": 90,
        "category": "main"
    },

    "manchurian": {
        "price": 400,
        "category": "starter"
    },

    "browni": {
        "price": 80,
        "category": "dessert"
    }
}


# Take budget from the user
user = int(input("Enter Budget: "))



budget_picks = [
    item
    for item, details in menu.items()
    if details["price"] < user
]


# Display Budget Picks
print("\nBudget Picks:", budget_picks)


# Select one random item from the menu
chef_pick = random.choice(list(menu.keys()))



print("Chef's Pick of the Day:", chef_pick)



dicti = {
    "main": [],
    "starter": [],
    "dessert": []
}



for key, value in menu.items():


    category = value["category"]


    dicti[category].append(key)



print("\nCategory Wise Menu:")


# Loop through each category and its items
for category, items in dicti.items():


    print("\n", category)


    total_price = 0



    for item in items:


        price = menu[item]["price"]


        print(item, "₹", price)


        total_price += price



    average_price = total_price / len(items)



    print("Average Price: ₹", f"{average_price:.2f}")