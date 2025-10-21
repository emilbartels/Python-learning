class Resturant:
    """A resturant that is very good"""
    
    def __init__(self, resturant_name, cuizine_style, number_served):
        self.resturant_name = resturant_name
        self.cuizine_style = cuizine_style
        self.number_served = number_served

    def describe_resturant(self):
        print(f'{self.resturant_name} is a very nice place that serves {self.cuizine_style}.')
    
    def open_resturant(self):
        print(f'{self.resturant_name} is open for business')

    def people_served(self):
        #Added en method som printer antal af numbered served
        print(f'So far we have served {self.number_served} people.')

    def set_number_served(self, set_number_served):
        #Added en method til at selv at ændre number served med et argument for methoden
        self.number_served = set_number_served

    def increment_number_served(self, increment):
        #Her kan man increment antal af personer served
        self.number_served += increment
        print(f'We have served {increment} people today')

resturant = Resturant('Livs køkken', 'waffles', 8)

print(f'My resturant is called {resturant.resturant_name}')
print(f'We serve {resturant.cuizine_style}')

resturant.open_resturant()
resturant.describe_resturant()

resturant.number_served = 111
resturant.people_served()

resturant.set_number_served(222)
resturant.people_served()

resturant.increment_number_served(10)
resturant.people_served()
