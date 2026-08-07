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

myCursor = conn.cursor()

sql = "SELECT name,song_count FROM playlist WHERE song_count > 10"
myCursor.execute(sql)

mylst = myCursor.fetchall()

print(mylst)

conn.commit()
conn.close()