# 1.Create a new Python file called playlist.py and define a function 
# add_song(song_name, playlist) that adds a song to the playlist list and returns the updated list.

def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist

songs = ["Jaanu", "Tu chahiye"]
result = add_song("Ram siya ram", songs)
print(result)

# 2.In a separate file main.py, import the add_song function from playlist.py and 
# use it to add three songs ('Kesariya', 'Shape of You', 'Believer') to an empty playlist, then print the final playlist.

def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist
playlist = []

add_song("Kesariya", playlist)
add_song("Ram lila", playlist)
add_song("jaane tu", playlist)
print(playlist)

# 3.Add a function remove_song(song_name, playlist) in playlist.py that removes a song if 
# it exists in the playlist and returns the updated list. Import and use this function in main.py 
# to remove 'Shape of You' from your playlist and print the result.

def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist

def remove_song(song_name, playlist):
    if song_name in playlist:
        playlist.remove(song_name)
    return playlist

playlist = []
add_song("Kesariya", playlist)
add_song("Shape of You", playlist)
add_song("Believer", playlist)

print("Before Remove = ", playlist)
remove_song("Shape of You", playlist)
print("After Remove = ", playlist)

# 4.Refactor your playlist.py by adding a function display_playlist(playlist) that prints 
# each song with its position number (like Spotify's queue). Import and use this function in 
# main.py after adding and removing songs.

def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist

def remove_song(song_name, playlist):
    if song_name in playlist:
        playlist.remove(song_name)
    return playlist

def display_playlist(playlist):
    for i in range(len(playlist)):
        print(i + 1, ".", playlist[i])

playlist = []
add_song("Hale dil", playlist)
add_song("Tere mere rishta", playlist)
add_song("Teri yaadoin main", playlist)

remove_song("Tera mera rishta", playlist)
display_playlist(playlist)