#Build a class named FoodOrder that represents a Zomato-style order with properties: restaurant_name, items (a list), and total_price. Add a method show_order() that prints the order details in a readable format.

class FoodOrder:
    def __init__(self,restaurant_name,items,total_price):
        self.restaurant_name=restaurant_name
        self.items=items
        self.total_price=total_price
    def show_order(self):
        print(self.restaurant_name)
        print(self.items)
        print(self.total_price)

order=FoodOrder("Star Chaines",["Paneer chilli","Grevy Manchurian","Fried Rice"],350)        
order.show_order()
                