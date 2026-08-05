#Write a Python class called InstagramPost with attributes caption, likes, and comments (a list). Add a method add_comment(comment_text) that appends a new comment to the comments list and increases the likes by 1.

class InstagramPost:
    def __init__(self,caption,likes,comments):
        self.caption=caption
        self.likes=likes
        self.comments=comments
    def add_comment(self,comment_text):
        self.comments.append(comment_text) 
        self.likes+=1 

Post=InstagramPost("My Frist Post",100,["cuite","great"])
Post.add_comment("Nice!")        

print(Post.caption)
print(Post.likes)
print(Post.comments)