#Create a new MySQL database called music_stream and a table called playlists with columns: id (INT, primary key, auto-increment), name (VARCHAR), and song_count (INT). Write a Python script using pymysql to insert three sample playlists into this table.

import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="music_stream"
)
if conn:
    print("connection succesfully")



mycursor = conn.cursor()
sql = "INSERT INTO playlist(name,song_count) VALUES (%s,%s)"
val= [
    ("Morning Vibes", 15),
    ("Chill Vibes", 20),
    ("Good Vibes", 5)
]



mycursor.executemany(sql,val)
mycursor.execute("SELECT * FROM playlist")
mylst = mycursor.fetchall()
print(mylst)
conn.commit()
conn.close()