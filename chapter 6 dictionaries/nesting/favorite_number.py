favorit_numbers = {
    'simon': [30, 27],
    'liv': [38, 27, 13],
    'lara': 77,
    'kobe bryant': [24, 8],
}


for name, numbers in favorit_numbers.items():
    
    #making the int to list
    if not isinstance(numbers, list):
        numbers = [numbers]

    if len(numbers) > 1:
        print(f"\nThis is {name.title()}'s favorite numbers:")
        for number in numbers:
            print(f'{number}')
    else:
        print(f"\nThis is {name.title()}'s favorite number:")
        for number in numbers:
            print(f'{number}')
