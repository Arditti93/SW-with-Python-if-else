order_1 = "Alex - Flat White"
order_2 = "Alice - Latte"
order_3 = "James - Black Coffee"

coffee_order = [
    "Alex - Flat White", 
    "Alice - Latte", 
    "James - Black Coffee",
]
print(coffee_order)
coffee_order[2] = "James - Hot Chocolate"
print(coffee_order)
coffee_order.append("Pete - Iced Latte")
print(coffee_order)
coffee_order.pop()
print(coffee_order)

coffee_order.pop(1)
print(coffee_order)

around_me = [
    "Speakers",
    "Bike",
    "Iphone"
]
print(len(around_me[2][-1]))
print(around_me[2][-1])