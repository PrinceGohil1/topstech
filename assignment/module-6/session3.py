# 1 Write a Python script that asks the user for 
# their name and favorite food using input(), 
# then prints a welcome message like 'Hello Priya, 
# your favorite food is Pizza!' using print().

name = input("Enter your name: ")
favorite_food = input("Enter your favorite food: ")

print(f"Hello {name}, your favorite food is {favorite_food}!")


# 2 Create a small program that takes two numbers as input 
# (use input()), converts them to integers using int(), 
# and prints their sum, difference, product, and quotient 
# using print().<br><br><em><strong>Hint:</strong> Remember 
# to convert the input strings to integers before performing 
# arithmetic operations.</em>

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("Sum =", sum_result)
print("Difference =", difference)
print("Product =", product)
print("Quotient =", quotient)


# 3 Build a Zomato-style bill calculator: take the price of a food 
# item and quantity as input, convert them to float and 
# int, calculate the total bill, and display it with a 
# message like 'Your total bill is ₹350.50'.

price = float(input("Enter the price of the food item (₹): "))
quantity = int(input("Enter the quantity: "))

total_bill = price * quantity

print(f"Your total bill is ₹{total_bill:.2f}")

# 4 Write a script that asks the user for their Instagram 
# follower count, converts it to an integer, and prints 
# the count in a formatted string like 'You have 1,500 
# followers'. Use escape characters to add a new line and 
# tab before the output.<br><br><em><strong>Hint:</strong> 
# Use '\n' for new line and '\t' for tab in your print 
# statement.</em>

followers = int(input("Enter your Instagram follower count: "))

print("\n\tYou have {:,} followers".format(followers))

# 5 Create a basic calculator program that takes two numbers 
# and an operator (+, -, *, /) as input, performs the correct 
# operation using typecasting, and prints the result. 
# If the user enters an invalid operator, print an error message.

num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print("Result =", result)

elif operator == "-":
    result = num1 - num2
    print("Result =", result)

elif operator == "*":
    result = num1 * num2
    print("Result =", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Error: Invalid operator. Please use +, -, *, or /.")