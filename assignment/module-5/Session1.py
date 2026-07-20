#1 Create a Python list named fav_items that 
# contains your favorite song name (string), your age (integer),
#  your monthly mobile data usage in GB (float), and a 
# boolean indicating if you have a premium subscription on any app

fav_items=["Kesariya",21,2.5,True]

print(fav_items)

#2 Update the fav_items list by changing the song name to another 
# song you like and increasing your age by 1.

fav_items=["Kesariya",21,2.5,True]
print(fav_items)

fav_items[0] = "Tu Chahiye"   
fav_items[1] = fav_items[1] + 1  

print(fav_items)

#3 Remove the mobile data usage value from fav_items using the del statement, 
# then print the updated list.<br><br><em><strong>Hint:</strong> 
# Use the index of the value you want to remove.</em>

fav_items=["Kesariya",21,2.5,True]

del fav_items[2]
print(fav_items)


#4Create a new list called weekend_plan with at least 5 items representing things you want 
# to do this weekend (mix of strings and numbers). Remove the last item using the pop() 
# method and display the removed item and the updated list


weekend_plan=["Watch a movie","Go for a walk",2,"Play cricket",500]

removed_item=weekend_plan.pop(2)
print("Removed Item = ",removed_item)
print("Updated List = ",weekend_plan)