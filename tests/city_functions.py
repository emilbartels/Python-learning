def city_country(city, country, population=''):
    """Generate some neatly formatted information about a city and country"""
    if population:
        city_country = f"{city}, {country}, population: {population}"
    else:
        city_country = f"{city}, {country}"
    return city_country.title()
