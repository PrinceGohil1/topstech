# 1.Given a list of cricket scores: [56.7, 102.3, 88.9, 45.2, 120.8], 
# use the round() function to create a new list with each score rounded
# to the nearest integer and print both the original and rounded lists.

# scores = [56.7, 102.3, 88.9, 45.2, 120.8]

# round_scores = []
# for score in scores:
#     round_scores.append(round(score))

# print("Original Scores = ", scores)
# print("Round Scores = ", round_scores)

# 2.Create a list of restaurant ratings (e.g., [4.2, 3.8, 4.9, 2.5, 4.0]) 
# and use the sorted() function to display the ratings in descending order.

# ratings = [4.2, 3.8, 4.9, 2.5, 4.0]
# sorted_ratings = sorted(ratings, reverse=True)

# print("Original Ratings:", ratings)
# print("Ratings in Descending Order:", sorted_ratings)

# 3.Write a program that takes a list of Flipkart product names and sorts 
# them alphabetically using the sort() method, then prints the sorted list.

# products=["Laptop", "Mobile", "Headphones", "Smartwatch", "Camera"]

# products.sort()
# print("Sorted Product List:", products)

# 4.You have two lists: one with Zomato restaurant names ['Burger Hub','Pizza Point','Sushi House']
#and another with their delivery times in minutes [30, 25, 40]. Use the zip() function
#to pair each restaurant with its delivery time and print each pair in the format:'Burger Hub - 30 min'.

# restaurants = ['Burger Hub', 'Pizza Point', 'Sushi House']

# delivery_times = [30, 25, 40]

# for restaurant, time in zip(restaurants, delivery_times):
#     print(restaurant, "-", time, "min")

# pairs = list(zip(restaurants, delivery_times))
# for i in pairs:
#     print(i[0], "-", i[1], "min")  


# 5.Build a function that takes two lists, one of YouTube video titles and one 
# of their view counts, and returns a list of tuples with each title and its 
# rounded view count (to the nearest thousand using round()).<br><br><em><strong>Hint:</strong> Use zip() to
# pair titles and counts, and round() inside a list comprehension.</em>

def video_views(titles, views):
    
    result = [(title, round(view, -3)) for title, view in zip(titles, views)]
    return result

titles = ["Python Tutorial", "Travel Vlog", "Gaming Highlights"]
views = [12540, 98765, 543210]

print(video_views(titles, views))