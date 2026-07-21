#1 Write a Python program that loops through a list of fruits: 
# ['Apple', 'Banana', 'Mango', 'Orange'] and prints each 
# fruit, but uses the continue statement to skip printing 'Banana'.

fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    if fruit == "Banana":
        continue
    print(fruit)

#2 Create a loop that goes through the following list: 
# ['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Burger King'], 
# and breaks the loop when it finds 'Burger King', printing 
# 'Found Burger King, stopping search.'

foods = ["Pizza", "Burger", "Pasta", "Sandwich", "Burger King"]

for food in foods:
    if food == "Burger King":
        print("Found Burger King, stopping search.")
        break
    print(food)

#3 Write a Python for loop that checks a list of playlists: 
# ['Chill Vibes', 'Workout', 'Focus', 'Party'], and uses 
# the pass statement when the playlist is 'Focus', but 
# prints all other playlist names.

playlists = ["Chill Vibes", "Workout", "Focus", "Party"]

for playlist in playlists:
    if playlist == "Focus":
        pass    # Do nothing
    else:
        print(playlist)

#4 Given a list of messages: ['Hi', 'Spam', 'Hello', 'Spam', 
# 'How are you?'], build a loop that prints only non-spam 
# messages by skipping any message that is 'Spam' using 
# continue, and stops reading further if the message 
# 'How are you?' is found using break.<br><br><em><strong>Hint:</strong> 
# Use both continue and break in the same loop for this task.</em>

messages = ["Hi", "Spam", "Hello", "Spam", "How are you?"]

for message in messages:
    if message == "Spam":
        continue      

    if message == "How are you?":
        print(message)
        break         

    print(message)

