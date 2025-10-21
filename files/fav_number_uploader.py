#10-11. Favorite Number: Write a program that prompts for the user’s favorite number. 
# Use json.dumps() to store this number in a file. 
# Write a separate program that reads in this value and prints the message “I know your favorite number! It’s ___.”

from pathlib import Path
import json

fav_number = input("Write your favorite number: ")
file = Path('fav_number.json')
contents = json.dumps(fav_number)
file.write_text(contents)