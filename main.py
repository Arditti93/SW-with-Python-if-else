music = "Rock Music" 

if music == "classical":
    print("oh no its classical")
elif music == "no music":
    print("Ah, peace and quiet")
else:
    print("Turn it up") 

music = "Dance Music" 
# != not equal to comparison operator
if music != "Britpop": 
    print("I want to listen to britpop")
else:
    print("I love britpop") 

music = "Oasis"

if music != "Britpop":
    print("I want to listen to Britpop")
elif music == "Oasis":
    print("Turn it up")
else:
    print("I love britpop")

temperature = 40

if temperature > 99:
    print("Its boiling")
elif temperature > 90:
    print("Its too hot")
elif temperature > 70:
    print("its warm")
elif temperature > 40:
    print("its just right")
else:
    print("its a bit chilly")


age = 18 
if age >= 18:
    print("Yes I can serve you")
else:
    print("You aren't old enough")


age = 6
if age <= 6:
    print("you can have a child ticket") 
else:
    print("sorry you are too old")


place = "Manchester"
weather  = "Sunny"

if place == "Manchester" and weather == "Sunny":
    print("Check Again")
elif place == "Manchester" and weather == "Rain":
    print("Obvs")
else:
    print("What? it isn't raining")

day = "Friday"
if day == "Saturday" or day == "Sunday":
    print("its the weekend")
else:
    print('its not the weekend')

