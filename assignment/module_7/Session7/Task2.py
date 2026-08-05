#Build a class Payment with a pay() method that takes amount as a parameter and prints 'Paying amount'. Then, create a subclass UPI that overrides pay() to print 'Paying amount via UPI'. Demonstrate both methods by making objects and calling pay().

class Payment:
    def __init__(self,amount):
        self.amount=amount
    def pay(self):
        print(f"Paying amount - {self.amount}")

class UPI(Payment):
    def __init__(self, amount):
        super().__init__(amount)
    def pay(self):
        print(f"Paying amount via UPI is - {self.amount}")    

p=Payment(100)
u=UPI(300)
p.pay()
u.pay()
