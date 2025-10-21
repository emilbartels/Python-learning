from pathlib import Path

path = Path('guest_book.txt')

guests = ''
name = ''

while True:
    name = input("Enter your name or quit to exit: ")

    if name.lower() == 'quit':
        break

    guests += f'{name.capitalize()}\n'

path.write_text(guests)