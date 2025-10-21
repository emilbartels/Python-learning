from city_functions import city_country

def test_city_country_population():
    """Does a city like copenhagen, in denmark, with 5000000 population work?"""
    formatted_city_country_population = city_country('Copenhagen', 'denmark', 500000)
    assert formatted_city_country_population == 'Copenhagen, Denmark, Population: 500000'