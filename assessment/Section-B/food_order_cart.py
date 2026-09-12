# Task 1: Order Cart Calculator
# Build a console program that manages a food order cart using lists, loops, and functions — the
# core of any ordering system.
# Store at least 6 menu items as a list of tuples (item_name, price); let the user add items to a
# cart list by entering item numbers in a loop that stops when the user types 'done'.
# Write a function calculate_total(cart) that iterates the cart list and returns the sum of all item
# prices.
# Apply 5% GST if the total is above Rs 300 and 18% GST if above Rs 600; display the base total,
# GST amount, and final payable amount.
# Print a formatted order summary showing each item name and price, the base total, GST rate
# applied, and the final payable amount.


food = [
    ("pizza", 200),
    ("burger", 100),
    ("bhel", 60),
    ("pavbhaji", 70),
    ("idli-smbhar", 40),
    ("dosa", 110)
]

cart = []


def total_cart(cart):
    total = 0

    for i in cart:
        total = total + i[1]

    if total > 600:
        gst_rate = 18
    elif total > 300:
        gst_rate = 5
    else:
        gst_rate = 0

    gst_amount = total * gst_rate / 100

    return total, gst_amount


print("========== MENU ==========")
print("1. Pizza - RS 200")
print("2. Burger - RS 100")
print("3. Bhel - RS 60")
print("4. Pavbhaji - RS 70")
print("5. Idli-sambhar - RS 40")
print("6. Dosa - RS 110")


while True:
    user = input("Enter item number: ")

    if user == "1":
        cart.append(food[0])
        print(cart)

    elif user == "2":
        cart.append(food[1])
        print(cart)

    elif user == "3":
        cart.append(food[2])
        print(cart)

    elif user == "4":
        cart.append(food[3])
        print(cart)

    elif user == "5":
        cart.append(food[4])
        print(cart)

    elif user == "6":
        cart.append(food[5])
        print(cart)

    elif user.lower() == "done":
        break

    else:
        print("Invalid item number. Please try again.")


total, gst = total_cart(cart)

print("Base Total:", total)
print("GST:", gst)
print("Final Total:", total + gst)