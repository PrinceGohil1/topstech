cart = [
    ("Pizza", 250),
    ("Burger", 120),
    ("Pasta", 200),
    ("Fries", 100),
    ("Biryani", 300)
]

count = 0
subtotal = 0

for item, price in cart:
    if price > 150:
        print(item, price)
        count += 1
        subtotal += price

print("Number of items:", count)
print("Subtotal:", subtotal)