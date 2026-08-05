#3.Add 2 more song names to my_fav_songs.txt without deleting the existing content, using Python's open() function in append ('a') mode.

f=open("my_fav_songs.txt","a")
f.write("\nTeri yaadon mein")
f.write("\nPrem ki leela")
f.close()
print("songs added successfully.")