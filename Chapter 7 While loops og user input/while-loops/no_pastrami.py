#“7-9. No Pastrami: 
# Using the list sandwich_orders from Exercise 7-8, 
# make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
#  and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
# Make sure no pastrami sandwiches end up in finished_sandwiches.”


sandwich_orders = ['diavola', 'pastrami', 'el diablo', 'pastrami', 'pastrami', 'pastrami',]

finished_sandwiches = []

print('The deli has run out of pastrami. We are very sorry!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()

    print(f'\nWe are preparing for the {finished_sandwich}')

    finished_sandwiches.append(finished_sandwich)

print(f'\nIf your sandwich is called, it is ready:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())