from city_functions import city_country

def test_city_country():
    """Does cities like copenhagen and denmark work, with population of 500000"""
    formatted_city_country = city_country('copenhagen', 'denmark')
    assert formatted_city_country == 'Copenhagen, Denmark'

