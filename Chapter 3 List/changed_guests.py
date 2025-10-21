#“3-5. Changing Guest List: 
# You just heard that one of your guests can’t make the dinner, 
# so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.

#Start with your program from Exercise 3-4. 
# Add a print() call at the end of your program, 
# stating the name of the guest who can’t make it.
#Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#Print a second set of invitation messages, one for each person who is still in your list.”

guests = ['Micheal jordan', 'Magnus Vedel Villadsen', 'Liv Elisabeth Sonne-Clifford']

message = f'Hello {guests[0]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
message = f'Hello {guests[1]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
message = f'Hello {guests[2]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)

print(f"I guess {guests[1]}, couldn't make it too us \n")

guests[1] = 'William Leopold Westh'

message = f'Hello {guests[0]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
message = f'Hello {guests[1]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
message = f'Hello {guests[2]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)