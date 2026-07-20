# 1.Given two lists — one of product names and one of their prices — use the zip() 
# function to create a dictionary mapping each product to its price, then print the dictionary.

products = ["Mobile", "Laptop", "Headphones"]
prices = [15000, 50000, 2000]

product_price = dict(zip(products, prices))
print(product_price)

# 2.Write a loop that takes two lists: usernames and their follower counts, and manually 
# creates a dictionary (without using zip()) that maps each username to its follower count, 
# similar to how Instagram tracks followers.

usernames = ["raj_07", "ananya_08", "prince_21"]
followers = [1200, 2500, 1800]

insta_followers = {}
for i in range(len(usernames)):
    insta_followers[usernames[i]] = followers[i]

print(insta_followers)

# 3.Suppose you have two lists: one with IPL team names and another with their total points this season.
#  Use zip() to combine them into a dictionary, then print only the teams that have more than 10 points.
# <br><br><em><strong>Hint:</strong> After creating the dictionary, use a for loop to filter and print.</em>

teams = ["CSK", "MI", "GT", "RCB", "KKR"]
points = [12, 8, 14, 10, 16]

ipl_points = dict(zip(teams, points))

for team, point in ipl_points.items():
    if point > 10:
        print(team, "-", point, "points")

# 4.Given three lists — movie titles, genres, and ratings — use zip() to create a list of dictionaries
# where each dictionary contains keys 'title', 'genre', and 'rating' for a movie, then print the list.
# <br><br><em><strong>Constraint:</strong> Do not use any external libraries.</em>

titles = ["Pushpa", "KGF", "3 Idiots"]
genres = ["Action", "Action", "Comedy"]
ratings = [8.2, 8.5, 9.0]

result = list(zip(titles, genres, ratings))

movies = []

for i in range(len(result)):
    movies.append({
        "title": result[i][0],
        "genre": result[i][1],
        "rating": result[i][2]
    })

print(movies)