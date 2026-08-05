# Given the following code, fix it so that the Movie class overrides the display() method to show the movie's title and year, instead of just the title:<br><br>class Content:
# def display(self, title):
# print('Title:', title)

# class Movie(Content):
# def display(self, title, year):
# your code here<br><br>Call display() on a Movie object with both title and year.

class Content:
    def display(self, title):
        print("Title :", title)

class Movie(Content):
    def display(self, title, year):
        print("Title :", title)
        print("Year :", year)

m = Movie()
m.display("DON", 1978)