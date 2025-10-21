def city_country(city, country):
    """Here is a function which takes a city and a country pair and prints it"""
    cityincountry = (f'{city.title()}, {country.title()}')
    return cityincountry
dk = city_country('copenhagen', 'denmark')
print(dk)

brazil = city_country('rio de janioro', 'brazil')
print(brazil)