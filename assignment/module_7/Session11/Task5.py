# Suppose you want to build a 'Recently Played' feature like Spotify. Write a Python function using pymysql that deletes a playlist from the playlists table by its id, and handles the case where the id does not exist by printing an appropriate message.<br><br><em><strong>Constraint:</strong> Use try-except to handle errors and close the connection properly in all cases.</em>

import pymysql

def delete_playlist():
    conn = None

    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="rootroot",
            database="music_stream"
        )

        mycursor = conn.cursor()

        user_id = int(input("Enter playlist id: "))

        sql = "DELETE FROM playlist WHERE id = %s"
        mycursor.execute(sql, (user_id,))

        if mycursor.rowcount > 0:
            conn.commit()
            print("Playlist deleted successfully")
        else:
            print("Playlist id does not exist")
    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            conn.close()
            print("Connection closed")

delete_playlist()