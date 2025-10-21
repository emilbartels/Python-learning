#7-10. Dream Vacation: 
# Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll.”


responses = {}

flag_active = True

while flag_active:
#Prompt for responses:
    name = input(f'\nWhat is your name?')
    place = input(f'Where would you like to go, if you could go anywhere?')

    responses[name] = place

    repeat = input(f'\nWould you let another person answer the interview? (Yes / No)')

    if repeat == 'no':
        flag_active = False



for name, place in responses.items():
    print(f'{name} would really like to visit {place} some time in their life')







    
