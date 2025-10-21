#“3-6. More Guests: 
# You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.

#Start with your program from Exercise 3-4 or 3-5. 
# Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

guests = ['Micheal jordan', 'Magnus Vedel Villadsen', 'Liv Elisabeth Sonne-Clifford']

message = f'Hello {guests[0]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
message = f'Hello {guests[1]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
message = f'Hello {guests[2]} are hereby invited to a dinner at my house. I would be honored to see you there\n'
print(message)

print(f"I have found a bigger table so i will add more people to the list. Looking forward to seeing y'al\n")
guests.insert(0, 'William Leopold Westh')
guests.insert(3, 'Simon Bartels Sørensen')
guests.append('Sebastian Holmberg')

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
message = f'Hello {guests[5]} are hereby invited to a dinner at my house. I would be honored to see you there'
print(message)
