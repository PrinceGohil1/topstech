#Arrange four buttons in a 2x2 grid layout using Tkinter's grid() method, similar to how calculator buttons are placed. Label the buttons as 'Like', 'Share', 'Download', and 'Add to Queue'.

import tkinter as tk

root = tk.Tk()
root.title("Music Controls")
root.geometry("350x200")

like_button = tk.Button(root, text="Like", width=15)
like_button.grid(row=0, column=0, padx=10, pady=10)

share_button = tk.Button(root, text="Share", width=15)
share_button.grid(row=0, column=1, padx=10, pady=10)

download_button = tk.Button(root, text="Download", width=15)
download_button.grid(row=1, column=0, padx=10, pady=10)

queue_button = tk.Button(root, text="Add to Queue", width=15)
queue_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
