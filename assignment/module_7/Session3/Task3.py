#Create a function book_movie_ticket that takes the number of tickets as input and divides a fixed wallet balance by the number of tickets to get the price per ticket. Handle ZeroDivisionError and ValueError using multiple except blocks, and print a different message for each error.<br><br><em><strong>Hint:</strong> Use two separate except blocks for ZeroDivisionError and ValueError.</em>

def book_movie_ticket(ticket):
    wallet=1000/ticket
    return wallet
try:
    tickets=int(input("Enetr Number of tickets = "))

    print(book_movie_ticket(tickets))

except ZeroDivisionError:
    print("Number of ticket cannot be zero!!!")

except ValueError:
    print("Please Enter valid number!!!")    