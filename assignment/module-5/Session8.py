# 1.Write a Python function called calculate_total that takes two positional 
# arguments: price and quantity, and returns their product. Call the function 
# with price=120 and quantity=3, and print the result.

def calculate_total(price, quantity):
    return price * quantity

ans= calculate_total(120, 3)
print(ans)

# 2.create a function called format_username that takes a username (positional argument)
# and an optional prefix (default value 'user_'). The function should return the username wit
# the prefix added. Test the function with and without providing the prefix.

def format_username(username, prefix="user_"):
    return prefix + username

print(format_username("prince"))
print(format_username("prince", "admin_"))

# 3.Build a function book_movie_ticket(movie_name, seat_type='Regular', snacks=None) that prints a booking summary. 
# Call the function using only positional arguments, only keyword arguments, and a mix of both to book tickets for 
# 'Jawan' and 'Pathaan' with different seat types and snacks.
# <br><br><em><strong>Hint:</strong> Try calling book_movie_ticket('Jawan', snacks='Popcorn', seat_type='VIP')</em>

def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):
    print("Movie Name = ")
    print("Seat Type  = ")
    print("Snacks     = ")
    print("------------------------")

book_movie_ticket("Jawan", "VIP", "Popcorn")

book_movie_ticket(movie_name="Pathaan", seat_type="Premium", snacks="Cold Drink")

book_movie_ticket("Jawan", snacks="Popcorn", seat_type="VIP")

# 4.Write a function called apply_coupon(amount, coupon_code=None) that applies a 10% discount if 
# coupon_code is 'SAVE10'. Test the function with and without passing the coupon_code argument.
# <br><br><em><strong>Constraint:</strong> Use a default value for coupon_code so the function 
# works even if no coupon is provided.</em>

def apply_coupon(amount, coupon_code=None):

    if coupon_code == "SAVE10":
        discount = amount * 10 / 100
        amount = amount - discount
    return amount

print(apply_coupon(1000, "SAVE10"))
print(apply_coupon(1000))