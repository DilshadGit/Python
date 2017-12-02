#!/usr/bin/python

foods = ['Beef', 'Fish', 'Bread', 'Vegitable', 'Milk']

for food in foods:
    print("I like ", food)

foods.append('Tomatos')
foods.append('Chicken')

print(foods)

foods.remove('Bread')

print(foods)

# In the index 2 we insert orange
foods.insert(2, 'Orange')
foods.insert(6, 'Apple')

print(foods)