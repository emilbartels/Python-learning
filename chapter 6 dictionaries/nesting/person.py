person_0 = {
    'first name': 'Liv', 
    'last name': 'Sonne-Clifford', 
    'age': 20, 
    'city': 'Tårnby', 
            }
person_1 = {
    'first name': 'Emil', 
    'last name': 'Bartels', 
    'age': 20, 
    'city': 'Tårnby',
            }
person_2 = {
    'first name': 'David', 
    'last name': 'Veistrup', 
    'age': 20, 
    'city': 'Ørestad',
}

people = [person_0, person_1, person_2]

for person in people:
    print(f'\nHer er det jeg ved om {person['first name']}')
    for key, value in person.items():
        print(f' {key.title()}: {value}')
