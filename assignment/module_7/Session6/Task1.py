#Create a Python class called User with attributes username and email, then create an object and print its details.

class user:
    def __init__(self,username,email):
        self.username=username
        self.email=email

    def display(self):
        print(f"{self.username} - {self.email}") 

u1=user("prince","p@gmail.com")
u1.display()           