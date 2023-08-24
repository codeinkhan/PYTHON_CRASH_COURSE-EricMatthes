#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

my_foods=['Pav Bhaji','Biryani','Gulab Jamun','Korean Chicken','Blueberry Cheesecake',]

friends_foods=my_foods[:]

print('My Favorite Foods Are : ')
for food in my_foods:
    print(food)
print('\n')
print('Friends Favorite Foods Are : ')
for food in friends_foods:
    print(food)
