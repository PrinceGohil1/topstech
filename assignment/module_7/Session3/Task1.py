#Write a Python function get_song_duration that takes a song name and returns its duration from a predefined dictionary. Use a try-except block to handle the case where the song is not found and print 'Song not found on Spotify!'
def get_song_duration(song_name):
    songs={"Tera Chehra":"4:59",
           "Bolna":"3:23",
           "Dil":"3:11"}
    try:
        final=songs[song_name]
        return final
    except KeyError:
        print("Song not found on Spotify!")
           
song=input("Enter song name = ")
print(get_song_duration(song))