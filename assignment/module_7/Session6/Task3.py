#Demonstrate multilevel inheritance by creating a class VerifiedInfluencer that inherits from Influencer and adds a badge attribute; create a VerifiedInfluencer object and display all its properties.

class user:
    def __init__(self,username,email):
        self.username=username
        self.email=email

class Influencer(user):
    def __init__(self, username, email,followers):
        super().__init__(username, email)  
        self.follower=followers

class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers,badge):
        super().__init__(username, email, followers)
        self.badge=badge

    def display(self):
        print(f"{self.username} - {self.email} - {self.follower} - {self.badge}")  

p1=VerifiedInfluencer("Prince","p@gmail.com",2000,"verified")                    
p1.display()