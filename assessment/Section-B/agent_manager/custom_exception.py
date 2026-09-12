# Build an OOP-based console tool that models delivery agents, enforces order limits using a
# custom exception, and logs all assignments to a file.
# Create a DeliveryAgent class with __init__(name, phone) setting name, phone, and an empty
# orders list; add an assign_order(order_id) method that appends to the list.
# Subclass SeniorAgent from DeliveryAgent, adding a performance_score attribute (float);
# override assign_order() to also print the agent's current score before assigning.
# Python • M4 - DB and Python Framework • M4-A1 Page 3
# ASSESSMENT FILE
# Python
# M4-A1
# Define a custom exception MaxOrdersExceeded(Exception) and raise it inside assign_order() if
# the agent already has 5 or more active orders.
# Wrap all file writes to agents_log.txt (append mode) in try/except/finally; the finally block must
# close the file; catch MaxOrdersExceeded separately and log the error message to the file
# rather than crashing.

class MaxOrdersExceeded(Exception):
    pass


class DeliveryAgent:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.orders = []

    def assign_order(self, order_id):
        if len(self.orders) >= 5:
            raise MaxOrdersExceeded("Maximum 5 orders allowed")

        self.orders.append(order_id)


class SeniorAgent(DeliveryAgent):
    def __init__(self, name, phone, performance_score):
        super().__init__(name, phone)
        self.performance_score = float(performance_score)

    def assign_order(self, order_id):
        print("Performance score:", self.performance_score)
        super().assign_order(order_id)


agent = SeniorAgent("Parth", "9876543210", 95.5)

order_ids = [101, 102, 103, 104, 105, 106]

for order_id in order_ids:

    file = None

    try:
        file = open("agents_log.txt", "a")

        agent.assign_order(order_id)

        file.write(
            f"Agent: {agent.name}, "
            f"Phone: {agent.phone}, "
            f"Order: {order_id}, "
            f"Status: Assigned\n"
        )

        print("Order assigned:", order_id)

    except MaxOrdersExceeded as e:
        print("Error:", e)

        if file:
            file.write(
                f"Agent: {agent.name}, "
                f"Order: {order_id}, "
                f"Error: {e}\n"
            )

    except Exception as e:
        print("Unexpected error:", e)

        if file:
            file.write(
                f"Unexpected Error: {e}\n"
            )

    finally:
        if file:
            file.close()