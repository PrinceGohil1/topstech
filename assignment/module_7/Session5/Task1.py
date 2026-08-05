#Create a Python class called Song with attributes title, artist, and duration (in seconds). Use the __init__ method to initialize these attributes and create two Song objects with different values.

class song:
    def __init__(self,title,artist,durataion):
        self.title = title
        self.artist = artist
        self.duration = durataion
p1 =  song("Haan tu hai","Pritam",5.24)
p2 =  song("Hale dil","harshit",5.46)
print(p1.title,p1.artist ,p1.duration)
print(p2.title,p2.artist ,p2.duration)     