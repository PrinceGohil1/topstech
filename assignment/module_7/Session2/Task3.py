#3.Simulate a Zomato-style order history: create a file orders.txt with at least 5 lines (each line is an order). Write a script that reads and prints each order line-by-line using a loop, and after reading each line, prints the file pointer's position using tell().

file = open("orders.txt", "r")
while True:
    order = file.readline()

    if order == "":
        break
    print(order.strip())
    print("Pointer Position =", file.tell())

file.close()