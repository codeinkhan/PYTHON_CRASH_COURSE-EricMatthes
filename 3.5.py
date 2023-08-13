#3-5. Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations.
#         You'll have to think of someone else to invite. Start with your prograin from Exercise 3-4. Add a print() call at the end of your program,
#         stating the name of the guest who can't make it. Modify your list, replacing the name of the guest who can't make it with the name of
#         the new person you are inviting Print a second set of invitation messages, one for each person who is still in your list.

names=["alexandar the great","chengis khan","adolf hitler","winston churchill","abraham lincoln"]
print("You are cordially invited to join us for a special event. Please join "+names[0].title()+", "+names[1].title()+" and  "+names[2].title()+" for an unforgettable time together.")

print("Sorry to say but "+names[2].title()+" may not be able to join the meeting.")
names[2]="ratan tata"
print("Instead "+names[2].title()+" will be joining us.")
