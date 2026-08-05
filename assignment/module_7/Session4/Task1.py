#Create a custom exception class called InvalidCouponCodeError for a Zomato-style food ordering app, and raise this exception if a user tries to apply a coupon code that is not in the list of valid codes.

class InvalidCouponCodeError(Exception):
    pass
codes= ["ZOMATO50", "FOOD20", "SAVE100"]

try:
    coupon = input("Enter Coupon Code = ")
    if coupon not in codes:
        raise InvalidCouponCodeError

    print("Coupon Applied Successfully!")

except InvalidCouponCodeError:
    print("Invalid Coupon Code!")