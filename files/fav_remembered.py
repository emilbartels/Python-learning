from pathlib import Path
import json

file = Path('your_fav_number.json')

if file.exists():
    content = file.read_text()
    fav_number = json.loads(content)
    print(f"Your favorite number is {fav_number}")

else:
    fav_number = input("Write your favorite number: ")
    contents = json.dumps(fav_number)
    file.write_text(contents)