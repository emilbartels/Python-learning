class Resturant:
    """A resturant that """
    
    def __init__(self, resturant_name, cuizine_style):
        self.resturant_name = resturant_name
        self.cuizine_style = cuizine_style

    def describe_resturant(self):
        print(f'{self.resturant_name} is a very nice place that serves {self.cuizine_style}')
    
    def open_resturant(self):
        print(f'{self.resturant_name} is open for business')