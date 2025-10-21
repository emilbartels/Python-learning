from pathlib import Path

catfile = Path('cats.txt')
dogfile = Path('dogs.txt')
try:
    cat_contents = catfile.read_text()
    print("Here is the cat file:")
    print(cat_contents.capitalize())
except FileNotFoundError:
    print("The catfile doesnt exist")

try:
    dog_contents = dogfile.read_text()

    print(f"\nHere is the dog file:")
    print(dog_contents.capitalize())
except FileNotFoundError:
    pass