#Organize your code by creating a package called insta_utils with two modules: likes.py (function: like_count(current, increment)) and comments.py (function: comment_count(current, new_comments)). In a main.py file, import both modules and simulate updating likes and comments for a post.

from package import likes,comments

current_likes = 120
current_comments = 35

updated_likes = likes.like_count(current_likes, 10)
updated_comments = comments.comment_count(current_comments, 5)

print(f"Updated Likes : {updated_likes}")
print(f"Updated Comments : {updated_comments}")