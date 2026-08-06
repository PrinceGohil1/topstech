import random
from song import song_list

random.shuffle(song_list)

for song in song_list:
    print(song)