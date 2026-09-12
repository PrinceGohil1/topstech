sales = {
    "Mumbai": {
        "Pizza": 50,
        "Burger": 30,
        "Pasta": 20
    },
    "Surat": {
        "Dhokla": 40,
        "Khaman": 25
    }
}

dishes = [
    dish
    for restaurant, menu in sales.items()
    if restaurant == "Mumbai"
    for dish in menu
]

print(dishes)