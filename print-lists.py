import random

food = ["pizza", "pie", "apples", "juice", "mustard", "orange", "soy sauce"]

print(food[5])

names = ["George", "Sam", "Hector", "Ellie", "Kate"]
print(names[random.randint(0, 5)])

side = ["fries", "onion rings", "apples slices", "chips"]
main_course = ["burger", "pizza", "chicken", "pasta", "steak"]
dessert = ["ice cream", "lava cake", "cupcake", "chocolate chip cookies"]

print(side[random.randint(0, 4)] + main_course[random.randint(0, 5)] + dessert[random.randint(0, 4)])
