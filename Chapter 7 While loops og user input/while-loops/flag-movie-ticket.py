prompt = f'\nHow old are you?\n'
prompt += 'Enter "quit" to end the program: '


active = True
while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        age = int(age)

    ticket = ""
    
    if age < 3:
        ticket = 0
        print(f'Since you are {age} years old, the ticket will be free.')
    elif age < 12:
        ticket = 10
        print(f'Since you are {age} years old, the ticket will be {ticket} dollars.')
    elif age >= 12:
        ticket = 15
        print(f'Since you are {age} years old, the ticket will be {ticket} dollars.')