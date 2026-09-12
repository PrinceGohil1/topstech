
class DeliveryPartner:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.active_orders = []

    def assign_order(self, order):
        self.active_orders.append(order)

        print("Order assigned successfully.")
        print("Partner Name:", self.name)
        print("Phone:", self.phone)
        print("Order ID:", order)


class SeniorPartner(DeliveryPartner):

    def __init__(self, name, phone, performance_score):
        super().__init__(name, phone)
        self.performance_score = performance_score

    # Method overriding
    def assign_order(self, order):

        print("Senior Partner")
        print("Performance Score:", self.performance_score)

        self.active_orders.append(order)

        print("Order assigned successfully.")
        print("Partner Name:", self.name)
        print("Phone:", self.phone)
        print("Order ID:", order)


# Creating normal DeliveryPartner object
partner1 = DeliveryPartner("Rahul","9876543210")
partner1.assign_order(101)
print("Active Orders:", partner1.active_orders)
print("\n")

# Creating SeniorPartner object
partner2 = SeniorPartner("Amit","9876501234",4.8)
partner2.assign_order(201)
print("Active Orders:", partner2.active_orders)

