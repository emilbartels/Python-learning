rivers = {'nile': 'egypt', 'amazonas': 'brazil', 'yangtze': 'china', 'yangtze': 'china'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for river in rivers.keys():
    print(f"\n{river.title()}")

for country in rivers.values():
    print(f"\n{country.title()}")