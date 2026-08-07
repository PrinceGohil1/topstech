#Add three buttons to your Tkinter window labeled 'Play', 'Pause', and 'Next'. When each button is clicked, update a label below the buttons to show which action was selected (e.g., 'Playing', 'Paused', 'Next Song').

import tkinter as tk

root = tk.Tk()
root.title("My Playlist")
root.geometry("400x200")

status_label = tk.Label(root, text="Select an action")
status_label.pack(pady=10)

def play():
    status_label.config(text="Playing")

def pause():
    status_label.config(text="Paused")

def next_song():
    status_label.config(text="Next Song")

play_button = tk.Button(root, text="Play", command=play)
play_button.pack()

pause_button = tk.Button(root, text="Pause", command=pause)
pause_button.pack()

next_button = tk.Button(root, text="Next", command=next_song)
next_button.pack()

root.mainloop()