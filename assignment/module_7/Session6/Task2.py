#Build a single inheritance example where a class Influencer inherits from User and adds a followers attribute; create an Influencer object and print all its details.

class user:
    def __init__(self,username,email):
        self.username=username
        self.email=email

class Influencer(user):
    def __init__(self, username, email,followers):
        super().__init__(username, email)  
        self.follower=followers

    def display(self):
        print(f"{self.username} - {self.email} - {self.follower}")  

p1=Influencer("Prince","p@gmail.com",2000)                    
p1.display()