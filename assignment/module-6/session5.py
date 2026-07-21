#1 Write a Python script that uses a for loop to print out 
# the names of five food delivery apps you use 
# (like Zomato, Swiggy, Domino's, McDonald's, Pizza Hut), 
# one per line.

food_apps = ["Zomato", "Swiggy", "Domino's", "McDonald's", "Pizza Hut"]

for app in food_apps:
    print(app)


#2 Given the string user_bio = 'Music lover | Foodie | Traveller', 
# use a for loop to count and print the number of characters 
# (excluding spaces) in the bio.<br><br><em><strong>Hint:
# </strong> Use an if statement inside the loop to skip 
# spaces.</em>

user_bio = "Music lover | Foodie | Traveller"

count = 0

for char in user_bio:
    if char != " ":   # Skip spaces
        count += 1

print("Number of characters (excluding spaces):", count)

#3 Create a list called fav_movies with the names of your 
# three favorite movies. Use a for loop to print each movie 
# name in uppercase letters.

fav_movies = ["3 Idiots", "KGF", "Bahubali"]

for movie in fav_movies:
    print(movie.upper())

#4 Build a Python script that asks the user to enter a word 
# (like a song name), then uses a for loop to print each 
# character on a new line, but only if the character is a 
# vowel (a, e, i, o, u).<br><br><em><strong>Constraint:
# </strong> Do not use the 'in' operator inside your 
# if statement — use multiple '==' checks instead.</em>

word = input("Enter a word (e.g., a song name): ")

for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
       ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        print(ch)