#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#        Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#        Use insert() to add one new guest to the beginning of your list. Use insert() to add one new guest to the middle of your list.
#        Use append() to add one new guest to the end of your list.. Print a new set of invitation messages, one for each person in your list.

names=["alexandar the great","chengis khan","adolf hitler"]
print("You are cordially invited to join us for a special event. Please join "+names[0].title()+", "+names[1].title()+" and  "+names[2].title()+" for an unforgettable time together.")

names.insert(0,"ratan tata")
names.append("elon musk")
names.append("albert einstein")
print ("I am Happy to say that we have 3 more seats avaiable, and I am delighted to invite "+names[0].title()+", "+names[4].title()+" and "+names[5].title()+".")
