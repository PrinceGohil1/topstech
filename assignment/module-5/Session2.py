# 1.Create a Python list called playlist containing five of 
# your favorite song names, then use a for loop to print each 
# song with its position in the playlist (starting from 1).

playlist=["Tu Chahiye","Apna Bana Le","Tum Hi Ho","Heeriye","Perfect"]

for i in range(len(playlist)):
    print(i + 1, ".", playlist[i])



# 2.Given a list of food items ordered on Zomato: 
# foods = ['Pizza', 'Burger', 'Dosa', 'Pasta', 'Fries'], 
# use a for loop with range() to print only the first three items in the list.

foods = ['Pizza', 'Burger', 'Dosa', 'Pasta', 'Rices']

for i in range(3):
    print(foods[i])

#3.Simulate a Flipkart shopping cart: prices = [299, 499, 150, 1200, 350].
#Use a for loop to calculate and print the total cart value.

prices = [299, 499, 150, 1200, 350]

total = 0
for price in prices:
    total = total + price

print("Total Cart Value =", total)

# 4.Build a WhatsApp-style unread messages counter: given a list
#  unread_counts = [2, 0, 15, 120, 5], use a for loop to print '99+' 
#  if the count is greater than 99, otherwise print the actual count for each chat.

unread_counts = [2, 0, 15, 120, 5]

for count in unread_counts:
    if count > 99:
        print("99+")
    else:
        print(count)