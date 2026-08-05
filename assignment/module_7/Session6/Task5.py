#Refactor your VerifiedInfluencer class to include a method display_profile() that prints details in the format used on Instagram profiles (username, followers in K/M, badge status).<br><br><em><strong>Hint:</strong> Use a helper function to format large follower counts, e.g., 1500 as '1.5K'.</em>

class VerifiedInfluencer:
    def __init__(self, username, followers, badge_status):
        self.username = username
        self.followers = followers
        self.badge_status = badge_status

    def format_followers(self):
        if self.followers >= 1000000:
            return f"{self.followers/1000000:.1f}M"
        elif self.followers >= 1000:
            return f"{self.followers/1000:.1f}K"
        else:
            return str(self.followers)

    def display(self):
        print(f"{self.username} -  {self.format_followers()} - {self.badge_status}")

v = VerifiedInfluencer("prince_07", 15000, "Verified")
v.display()