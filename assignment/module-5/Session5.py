# 1.Create a Python dictionary called playlist with 
# three songs as keys and their durations (in seconds) as values. 
# Update the duration of one song and print the updated dictionary.

playlist = {
            "Tu mera janu hai": 240,
            "Tera chehra": 204,
            "Senorita": 191
           }

playlist["Tera chehra"] = 210
print(playlist)

# 2.Build a nested dictionary called user_profiles where each key is a username 
# (like 'raj_07', 'ananya_xo') and the value is another dictionary with keys:'followers','following',and'posts'. 
# Add data for at least two users and print the number of followers for 'ananya_xo'.

user_profiles = {
    "raj_07": {
        "followers": 1200,
        "following": 350,
        "posts": 45
    },
    "ananya_xo": {
        "followers": 2500,
        "following": 500,
        "posts": 80
    }
}
print(f"{"Followers of ananya_xo ="} {user_profiles["ananya_xo"]["followers"]}")

# 3.Simulate a Zomato-style restaurant menu using a nested dictionary: each restaurant name 
# as a key, and its value as another dictionary with keys 'cuisine' and 'rating'. Add two restaurants, 
# then update the rating of one restaurant to a new value.<br><br><em><strong>Hint:</strong> Use 
# dictionary indexing to access and update the nested 'rating' value.</em>

# Create a nested dictionary
restaurants = {
    "Pizza Point": {
        "cuisine": "Italian",
        "rating": 4.2
    },
    "Spice Villa": {
        "cuisine": "Indian",
        "rating": 4.5
    }
}
restaurants["Pizza Point"]["rating"] = 4.7
print(restaurants)

# 4.Given the following nested dictionary representing an IPL cricket team squad:<br><br>team 
# = {'CSK': {'captain': 'Dhoni', 'players': 18}, 'MI': {'captain': 'Rohit', 'players': 17}}<br><br>Write code to add 
# a new team 'GT' with captain 'Hardik' and 16 players, then print all team names and their captains

team = {
    "CSK": {"captain": "Dhoni", "players": 18},
    "MI": {"captain": "Rohit", "players": 17}
}

team["GT"] = {"captain": "Hardik", "players": 16}
for name, details in team.items():
    print(name, "-", details["captain"])