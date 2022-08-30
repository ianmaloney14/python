num1 = 42 #This is a variable
num2 = 2.3 #This is also a variable
boolean = True  #This is a boolean
string = 'Hello World'  #This is a variable called "String" with the string "Hello World" in it
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #This is an list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #This is a dictionary
fruit = ('blueberry', 'strawberry', 'banana')   #This is a tuple
print(type(fruit)) #This is a print function that prints the fruit tuple
print(pizza_toppings[1]) #This is a print function that prints the pizza_toppings list item in index position 1; which is Sausage
pizza_toppings.append('Mushrooms')  #This adds Mushrooms to the pizza_toppings list
print(person['name']) #This is a print function that prints the name John in the person dictionary
person['name'] = 'George'   #This sets the name in the person dictionary to George
person['eye_color'] = 'blue'   #This adds an eye color to the person dictionary 
print(fruit[2]) #This prints the fruit in index position 2 in the fuit tuple 

#This is a conditional that tells you if a number is greater than 45
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#This is a conditional that tells you if a word is less than 5 letters or greater than 15 letters. 
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

#This is a for loop that counts from 0 to 4
for x in range(5):
    print(x)

#This is a for loop that counts from 2 to 4
for x in range(2,5):
    print(x)

#This is a for loop that counts from 2 to 8 by 3
for x in range(2,10,3):
    print(x)


x = 0   #This assigns the value 0 to the variable x
#This is a while loop that increments x by 1 only while x < 5
while(x < 5):
    print(x)
    x += 1

#This removes the last indexed item from the pizza_toppings list
pizza_toppings.pop()
#This removes the item in index 1 from the pizza_toppings list
pizza_toppings.pop(1)

#This prints the person dictionary
print(person)
#This removes the eye_color item from the person dictionary
person.pop('eye_color')
#This prints the person dictionary
print(person)

#This is a for loop
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

#This is a function that prints hello 10 times
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

#This is a function that prints hello x amount of times
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

#This is a funtion that prints hello 10 times or x amount of times
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)