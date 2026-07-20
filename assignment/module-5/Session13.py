# 1.Use list comprehension to generate a list of 
# all even numbers between 10 and 50 (inclusive).

even_numbers = [i for i in range(10, 51, 2)]
print(even_numbers)

# 2.Given a list of playlists where each playlist is a list of 
# song durations in seconds (e.g., [[210, 180, 240], [150, 200], [300, 120, 90]]), 
# use a nested list comprehension to create a new list containing only the durations 
# greater than 200 seconds from all playlists.

playlists = [[210, 180, 240], [150, 200], [300, 120, 90]]

result = [j for i in playlists for j in i if j > 200]

print(result)

# 3.Build a list of tuples using list comprehension where each tuple contains a 
# Flipkart product name and its price, but only include products with prices above 
# 1000 from the given lists: names = ['Shoes', 'Bag', 'Watch', 'Headphones'], 
# prices = [999, 1500, 700, 2200].

names = ['Shoes', 'Bag', 'Watch', 'Headphones']
prices = [999, 1500, 700, 2200]

result = [(name, price) for name, price in zip(names, prices) if price > 1000]

print(result)

# 4.Given a matrix representing ratings for 3 Zomato restaurants by 4 users 
# (e.g., [[4, 5, 3, 2], [5, 4, 4, 3], [3, 2, 5, 5]]), use a nested list comprehension 
# to find all ratings above 4 and flatten them into a single list.<br><br><em><strong>Hint:
# </strong> You will need two for loops inside the list comprehension to flatten the matrix.</em>

ratings = [[4, 5, 3, 2],[5, 4, 4, 3],[3, 2, 5, 5]]

result = [rating for row in ratings for rating in row if rating > 4]
print(result)