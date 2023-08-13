#3-7. Shrinking Guest List: You just found out that your new dinner table won't arrive in time for the dinner, and now you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner. Use pop() to remove
# guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting
# them know you're sorry you can't invite them to dinner. Print a message to each of the two people still on your list, letting them know they're still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

names=["alexandar the great","chengis khan","adolf hitler"]
print("You are cordially invited to join us for a special event. Please join "+names[0].title()+", "+names[1].title()+" and  "+names[2].title()+" for an unforgettable time together.")

names.insert(0,"ratan tata")
names.append("elon musk")
names.append("albert einstein")
print ("\nI am Happy to say that we have 3 more seats avaiable, and I am delighted to invite "+names[0].title()+", "+names[4].title()+" and "+names[5].title()+".")

print(" I am sorry "+names[5]+",you are not invited to dinner")
names.pop(5)
print(" I am sorry "+names[4]+",you are not invited to dinner")
names.pop(4)
print(" I am sorry "+names[3]+",you are not invited to dinner")
names.pop(3)
print(" I am sorry "+names[2]+",you are not invited to dinner")
names.pop(2)
print("\nI am sorry to announce that I will be able to invite only "+names[0].title()+" & "+names[1].title())

del names[1]
del names[0]
print(names)
