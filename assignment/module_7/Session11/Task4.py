# Modify your script to update the name of a playlist in the playlists table (for example, change 'Chill Vibes' to 'Chill Hits') and print a message confirming the update.<br><br><em><strong>Hint:</strong> Use the UPDATE SQL statement and commit the changes.</em>


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
sql = "UPDATE playlist SET name = %s WHERE name = 'Morning Vibes'"
val= [
    ("Morning good")
]



mycursor.execute(sql,val)
mycursor.execute("SELECT * FROM playlist")
mylst = mycursor.fetchall()
print(mylst)
conn.commit()
print("Playlist name updated successfully")
conn.close()