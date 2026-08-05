#Write a function add_song_to_playlist(song_name, playlist) for a Spotify-like app that raises a SongAlreadyExistsError (custom exception) if the song is already present in the playlist.<br><br><em><strong>Hint:</strong> Define SongAlreadyExistsError as a user-defined exception class and use the raise keyword inside your function.</em>

class SongAlreadyExistsError(Exception):
    pass
def add_song_to_playlist(song_name, playlist):

    if song_name in playlist:
        raise SongAlreadyExistsError

    playlist.append(song_name)
    print("Song add successfully!!!") 
    return playlist

playlist=["Janu meri jaan","Chahat","Dil tere name"]         

try:
    song=input("Enter song name = ")
    add_song_to_playlist(song,playlist)

    print("playlist = ",playlist)

except SongAlreadyExistsError:
    print("Song already present in playlist!!!")    
