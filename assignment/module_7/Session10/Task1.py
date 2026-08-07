#Create a Tkinter window titled 'My Playlist' that displays a label saying 'Welcome to Your Music Playlist' at the top center of the window.

import tkinter as tk

root=tk.Tk()
root.title("My Playlist")
root.geometry("400x200")

label=tk.Label(root, text="Welcome to Your Music Playlist")
label.pack()

root.mainloop()