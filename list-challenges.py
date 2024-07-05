#---------------------------
#      Task 1
#---------------------------

# First, let's create a list. Notice the square brackets, and the , between each item!

favourite_websites = [
    "w3 Schools",
    "CodeWars",
    "Python Tutorial"
]

# To see the list, let's print it
# print(favourite_websites)

# .append() is a list method which allows you to add one item only to the end of a list
# there are other methods we could have used, like .extend() which allows us to add a list to a list
# favourite_websites.append("Real Python")
# favourite_websites.append("Udemy")

favourite_websites.extend(["Real Python","Udemy"])

# We can't see these changes being made, so let's print the list again to see the changes
# print(favourite_websites)

# .pop() removes the last item in the list by default

favourite_websites.pop()

# To see the changes to the list, let's print it again

# print(favourite_websites)

#---------------------------
#      Task 2
#---------------------------

shopping_list = [
    "apple",
    "carrot",
    "pizza",
    "carrot",
    "dog food",
    "orange juice",
    "egg",
    "kale",
    "carrot",
    "kale",
    "orange juice",
    "kale",
    "toilet roll",
    "stamps",
    "noodles",
    "pasta sauce",
    "egg",
    "pasta sauce"
]

# the .count() method allows me to specify a value, and it returns how many times that value appears in the list

# print(f"There are {shopping_list.count('egg')} eggs in the list")
# N.B -  If anyone does the above; the parser doesn't like the same quotes being used like this, and they'll get an error even though it looks right

# print(f"There are {shopping_list.count('egg')} eggs in the list")
# print(f"There are {shopping_list.count('kale')} kales in the list")
# print(f"There are {shopping_list.count('stamps')} stamps in the list")
# print(f"There are {shopping_list.count('carrot')} carrots in the list")
# print(f"There are {shopping_list.count('orange juice')} orange juices in the list")

#---------------------------
#      Task 3
#---------------------------

favourite_websites = [
    "w3 Schools",
    "CodeWars",
    "Python Tutorial"
    "Udemy",
    "Real Python"
]

#sort will sort the list alphabetically - but can sort it by reverse alphabetically, or by a function
# favourite_websites.sort(reverse=True)
# print(favourite_websites)
#this updates the list - from now on, it is in this order.
#To reverse print, put reverse=True in the sort paramter brackets

#count is a little different - while the others update the list, count doesn't. It just gets a property
favourite_websites=[
    "w3 Schools",
    "CodeWars",
    "Python Tutorial"
    "Udemy",
    "Real Python",
    "Udemy"
]

# print(favourite_websites.count("Udemy"))

#you might also see
# favcount=favourite_websites.count("Udemy")
# print(favcount)

#extend can add two lists together, or it can add multiple items to a list

fav_websitesb = [
    "Kaggle",
    "Learn Python"
]

favourite_websites.extend(fav_websitesb)
print(favourite_websites)

#we can do this with append - but append would make a list in a list - this keeps it workable!

#now, fav websites has also got all the items that were in fav_websitesb
# we can also add items that aren't in a list - it's more useful than append, because we can add more than one
# favourite_websites.extend(["DataQuest","LeetCode"])
# print(favourite_websites)
