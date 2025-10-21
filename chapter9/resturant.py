#“Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.”

class Resturant:
    """A resturant that """
    
    def __init__(self, resturant_name, cuizine_style):
        self.resturant_name = resturant_name
        self.cuizine_style = cuizine_style

    def describe_resturant(self):
        print(f'{self.resturant_name} is a very nice place that serves {self.cuizine_style}')
    
    def open_resturant(self):
        print(f'{self.resturant_name} is open for business')

resturant = Resturant('Livs køkken', 'waffles')

print(f'My resturant is called {resturant.resturant_name}')
print(f'We serve {resturant.cuizine_style}')
resturant.open_resturant()
resturant.describe_resturant()