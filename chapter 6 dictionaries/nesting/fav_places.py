favorite_places = {
    'liv': ['home', 'emils house', 'school'],
    'emil': ['gym', 'home', 'pc'],
    'seb': ['gym', 'pc', 'claras'],
}

for name, places in favorite_places.items():
    print(f"\nher er {name.title()}'s favorit steder at være:")
    for place in places:
        print(f'{place.title()}')