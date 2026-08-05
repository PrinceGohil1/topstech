#Simulate a Flipkart order summary calculator that takes price and quantity as input and calculates the total. Use try-except to handle ValueError if the user enters a non-numeric value, and display an error message.

try:
    price = float(input("Enter Price = "))
    quantity = int(input("Enter Quantity = "))

    total = price * quantity

    print("Total Amount =", total)

except ValueError:
    print("Please enter valid numeric values only!")