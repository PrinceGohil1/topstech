#2.Write a Python script that opens the my_fav_songs.txt file in read ('r') mode and prints each song name to the console with its line number (like a playlist).

f=open("my_fav_songs.txt","r")
num=1
for i in f:
    print(num,".",i.strip())
    num=num+1
f.close()    