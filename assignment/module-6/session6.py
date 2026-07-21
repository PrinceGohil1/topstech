#1 Use a while loop to print the numbers from 1 to 10, 
# each on a new line, in the console.

# count = 1

# while count <= 10:
#     print(count)
#     count += 1

#2 Build a simple Zomato-style offer countdown: 
# start with a variable 'minutes_left' set to 5, and use 
# a while loop to print 'Offer ends in X minutes' until it 
# reaches 0.

minutes_left = 5

while minutes_left > 0:
    print("Offer ends in", minutes_left, "minutes")
    minutes_left -= 1

print("Offer has ended!")

#3 Write a program using a while loop to print a right-angled 
# triangle star pattern with 5 rows, like:

row = 1

while row <= 5:
    star = 1
    while star <= row:
        print("*", end="")
        star += 1
    print()   # Move to the next line
    row += 1

#4 Simulate an infinite loading spinner in the console by 
# printing 'Loading...' repeatedly using a while True loop. Add a break condition to stop after 3 times.<br><br><em><strong>Hint:</strong> Use a counter variable and break when it reaches 3.</em>

count = 0

while True:
    print("Loading...")
    count += 1

    if count == 3:
        break

print("Loading complete!")

#5 Create a program that uses a while loop to print a pyramid 
# star pattern with 4 rows, so the output looks like 
# BookMyShow's seat rows:

rows = 4
i = 1

while i <= rows:
    # Print spaces
    spaces = 1
    while spaces <= rows - i:
        print(" ", end="")
        spaces += 1

    # Print stars
    stars = 1
    while stars <= (2 * i - 1):
        print("*", end="")
        stars += 1

    print()   # Move to the next line
    i += 1