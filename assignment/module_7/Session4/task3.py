#Simulate a Flipkart-style checkout process where a function process_payment(amount) raises a PaymentFailedError (custom exception) if the amount is less than or equal to zero, and prints 'Payment Successful' otherwise.

class PaymentFailedError(Exception):
    pass


def process_payment(amount):
    if amount <= 0:
        raise PaymentFailedError
    else:
        print("Payment Successful!!!")


try:
    user = int(input("Enter Amount = "))
    process_payment(user)

except PaymentFailedError:
    print("Payment Failed!!!")