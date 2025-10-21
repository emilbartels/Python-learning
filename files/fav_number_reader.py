# Write a separate program that reads in this value and prints the message “I know your favorite number! It’s ___.”

from pathlib import Path
import json

file = Path('fav_number.json')
content = file.read_text()
fav_number = json.loads(content)
print(f"I know your favorite number! It's {fav_number}.")