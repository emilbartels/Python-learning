#7-4. Pizza Toppings: 
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
# As they enter each topping, print a message saying you’ll add that topping to their pizza.”

prompt = 'What kind of toppings do you want to have on your pizza?\n'
prompt += 'Enter "quit" to end the program: '

message = ""

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(f'I will add {message} to the pizza')
