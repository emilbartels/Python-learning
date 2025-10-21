luis = {
    'name': 'luis',
    'owner': 'liv',
    'color': 'brown',
    'cuteness': '10/10',
    'danger': '4/10'
}

mango = {
    'name': 'mango',
    'owner': 'sebastian',
    'color': 'brown',
    'cuteness': '7/10',
    'danger': '8/10'
}

pets = [luis, mango]

for pet in pets:
    print(f'\nHer er alle informationerne om {pet["name"].title()}')
    for key, value in pet.items():
        print(f'{key.title()}: {value}')
