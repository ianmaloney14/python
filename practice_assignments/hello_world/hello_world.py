from operator import iand


print("Hello World!")

name = "Ian"

print("Hello", name)
print("Hello " + name)

x = 42
print("Hello", str(x))
print("Hello " + str(x))

fav_food1 = "Sushi"
fav_food2 = "Ramen"

print("I love to eat", fav_food1, "and", fav_food2)
print("I love to eat " + fav_food1, "and " + fav_food2)
print("I love to eat {} and {}." .format(fav_food1, fav_food2))
print(f"I love to eat {fav_food1} and {fav_food2}.")