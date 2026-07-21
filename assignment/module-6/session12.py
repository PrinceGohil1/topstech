#1 Define a function called get_discounted_price that 
# takes price and discount_percent as arguments and 
# returns the final price after applying the discount. 
# Test it with a price of 500 and a discount of 10%.

def get_discounted_price(price, discount_percent):
    discount = (price * discount_percent) / 100
    final_price = price - discount
    return final_price

price = 500
discount_percent = 10

result = get_discounted_price(price, discount_percent)
print("Final Price:", result)

#2 Write a function called format_follower_count that 
# takes a number and returns it in Instagram-style format 
# (e.g., 1500 as '1.5K', 1200000 as '1.2M').<br><br><em>
# <strong>Hint:</strong> Use if-elif-else to check the 
# number range and format accordingly.</em>

def format_follower_count(count):
    if count >= 1000000:
        return f"{count / 1000000:.1f}M"
    elif count >= 1000:
        return f"{count / 1000:.1f}K"
    else:
        return str(count)

print(format_follower_count(950))        
print(format_follower_count(1500))       
print(format_follower_count(1200000))    

#3 Given a list of song durations in minutes, use a lambda 
# function with the map() function to convert all durations 
# to seconds and print the resulting list.

song_durations = [3.5, 4.2, 2.8, 5.0, 3.9]

durations_in_seconds = list(map(lambda minutes: minutes * 60, song_durations))

print("Song durations in seconds:", durations_in_seconds)

#4 Use a lambda function with the filter() function to get 
# all product names from a Flipkart-style list that start 
# with the letter 'M'. Example list: ['Mobile', 'Mouse', 
# 'Laptop', 'Monitor', 'Keyboard'].

products = ["Mobile", "Mouse", "Laptop", "Monitor", "Keyboard"]

m_products = list(filter(lambda product: product.startswith("M"), products))

print("Products starting with 'M':", m_products)

#5 Using reduce() and a lambda function, calculate the 
# total bill amount for a Swiggy order given a list of 
# item prices: [120, 80, 150, 60].<br><br><em><strong>Hint:
# </strong> Import reduce from functools.</em>

from functools import reduce

item_prices = [120, 80, 150, 60]

total_bill = reduce(lambda x, y: x + y, item_prices)

print("Total Bill Amount:", total_bill)