#“3-7. Shrinking Guest List: 
# You just found out that your new dinner table won’t arrive in time for the dinner, 
# and now you have space for only two guests.

#Start with your program from Exercise 3-6. 
# Add a new line that prints a message saying that you can invite only two people for dinner.
#Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, 
# print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#Print a message to each of the two people still on your list, letting them know they’re still invited.
#Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of your program.”

# Original list
guests = ['Micheal jordan', 'Magnus Vedel Villadsen', 'Liv Elisabeth Sonne-Clifford']

# Print invites for all out 
message = f'Hello {guests[0]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
message = f'Hello {guests[1]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
message = f'Hello {guests[2]} are hereby invited to a dinner at my house. I would be honored to see you there\n'
print(message)

# Bigger table so i add more people to the list with append() and insert()
print(f"I have found a bigger table so i will add more people to the list. Looking forward to seeing y'al\n")
guests.insert(0, 'William Leopold Westh')
guests.insert(3, 'Simon Bartels Sørensen')
guests.append('Sebastian Holmberg')

# Print invites for all out 
message = f'Hello {guests[0]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
message = f'Hello {guests[1]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
message = f'Hello {guests[2]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
message = f'Hello {guests[3]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
message = f'Hello {guests[4]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
message = f'Hello {guests[5]} are hereby invited to a dinner at my house. I would be honored to see you there\n'
print(message)

# Smaller table for pop() and print the message to them
print(f"Shit, the table won't be here in time, so i have to only invite two people\n")
sad_guest = guests.pop(0)
print(f"I'm so sorry {sad_guest}, but I dont have space for you, so i retract my invitation")
sad_guest = guests.pop(1)
print(f"I'm so sorry {sad_guest}, but I dont have space for you, so i retract my invitation")
sad_guest = guests.pop(0)
print(f"I'm so sorry {sad_guest}, but I dont have space for you, so i retract my invitation")
sad_guest = guests.pop(-1)
print(f"I'm so sorry {sad_guest}, but I dont have space for you, so i retract my invitation\n")

print(f'You guys are still invited {guests[0]} and {guests[1]}. So see you here at our place')

del guests[0]
del guests[0]
print(guests)