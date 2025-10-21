favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

should_poll = ['william', 'simon', 'liv', 'kobe', 'sarah', 'jen']

for person in should_poll:
    if person in favorite_languages.keys():
        print(f'Thank you very much for responding to our poll already, {person.title()}')
    else:
        print(f'Hello, {person.title()}. You should take our poll.')