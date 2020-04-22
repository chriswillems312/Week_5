new_inventory = {"apples": 15, "bananas": 35, "grapes": 12}
print(new_inventory["bananas"])
new_inventory["oranges"] = 20
print(len(new_inventory))
print("grapes" in new_inventory)

def add_fruit(new_inventory, fruit, quantity=0) :
    new_inventory[fruit] = quantity
    print(new_inventory)

add_fruit(new_inventory, "strawberries", 10)
print("strawberries" in new_inventory)
print(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory["strawberries"])


