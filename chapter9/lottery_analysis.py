#Lottery Analysis: You can use a loop 
# to see how hard it might be to win 
# the kind of lottery you just modeled.
#Make a list or tuple called my_ticket.
#Write a loop that keeps pulling numbers
#until your ticket wins. 
# Print a message reporting how many times the loop
#  had to run to give you a winning ticket.

from random import choice
lotterynumbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
winning_numbers = []
my_tickets = []




x = 1
y = 1
t = 1


#Adder 4 random tal til ens egen tickets
print("The 4 numbers on your ticket is: ")
while t < 5:
    my_ticket = choice(lotterynumbers)
    my_tickets.append(my_ticket)
    t = t + 1
print(', '.join(map(str,my_tickets)))


print(f"\nIf your ticket matches these 4 letters and numbers wins a prize")

while x < 5:
    winning_number = choice(lotterynumbers)
    x = x +1
    winning_numbers.append(winning_number)
    
    if winning_numbers == my_tickets:
        print(f"You won with these numbers: {my_tickets}")
        print(f'It only took {y} tries')
        x = 8

    elif len(winning_numbers) == 4:
        y = y + 1
        winning_numbers.clear()
        x = 1


print(', '.join(map(str,winning_numbers)))
