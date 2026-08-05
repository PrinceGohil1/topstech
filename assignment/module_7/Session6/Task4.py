#Implement multiple inheritance by creating a class BrandPartner that inherits from both Influencer and a new class Brand (with attribute brand_name); create a BrandPartner object and print the username, followers, and brand_name.

class Influencer:
    def __init__(self,username,followers):
        self.username=username
        self.followers=followers

class Brand:
    def __init__(self,brand_name):
        self.brand_name=brand_name

class BrandPartner(Influencer,Brand):
    def __init__(self, username, followers,brand_name):
        Influencer.__init__(self,username,followers)
        Brand.__init__(self,brand_name)

    def display(self):
        print(f"{self.username} - {self.followers} - {self.brand_name}")

b=BrandPartner("Prince",2000,"Nike")
b.display()        