cities = {
    'københavn': {
        'beboere': '1 mil',
        'land': 'danmark',
        'fun fact': 'jeg bor her',
    },
    'aalborg': {
        'beboere': '0,2 mil',
        'land': 'danmark',
        'fun fact': 'fake aau der :D',
    },
    'hellerup': {
        'beboere': '0,05 mil',
        'land': 'danmark',
        'fun fact': 'de er rige her',
    },
}

for by, informationer in cities.items():
    print(f'\nHer er der nogle facts om {by.title()}')
    for titel, fact in informationer.items():
        print(f'{titel.title()}: {fact.capitalize()}')