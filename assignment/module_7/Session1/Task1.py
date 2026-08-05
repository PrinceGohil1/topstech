#1.Create a text file named my_fav_songs.txt using Python's open() function in write ('w') mode, and write the names of your 5 favorite songs into it, each on a new line

f=open("my_fav_songs.txt","w")
f.write("Tera chehra\n")
f.write("Dil ibaadat\n")
f.write("Tujhe sochta hoon\n")
f.write("Haan tu hai\n")
f.write("deva deva\n")
f.close()

print("Songs written successfully.")