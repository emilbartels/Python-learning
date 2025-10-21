
class Resturant:
    """A resturant that """
    
    def __init__(self, resturant_name, cuizine_style):
        self.resturant_name = resturant_name
        self.cuizine_style = cuizine_style

    def describe_resturant(self):
        print(f'{self.resturant_name} is a very nice place that serves {self.cuizine_style}')
    
    def open_resturant(self):
        print(f'{self.resturant_name} is open for business')

class Ice_cream_stand(Resturant):
    """A class that inherits attribiutes fra the parent class Resutrant."""

    def __init__(self, resturant_name, cuizine_style):
        #brug af super til at initialize parent attributes.
        super().__init__(resturant_name, cuizine_style)
        #Laver ny attribute til kun Ice_cream_stand class
        self.flavors = 'Vanilla', 'Strawberry', 'Straciatelle'
    
    def display_flavors(self):
       flavors = ' '.join(map(str, self.flavors))
       print(f'We got {flavors} ice cream')

ice_cream_stand = Ice_cream_stand("Liv's køkken", "dessert")

ice_cream_stand.describe_resturant()
ice_cream_stand.open_resturant()
ice_cream_stand.display_flavors()