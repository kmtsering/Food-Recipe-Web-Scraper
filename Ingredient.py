class Ingredient:
    '''
    Holds recipe data 
    '''
    def __init__(self, quantity, unit, name):
        '''
        Handles base case of 3 arguments for ingredient data.
        '''
        self.quantity = quantity
        self.unit = unit
        self.name = name
    
    def __init__(self, quantity, unit, name, description):
        '''
        Handles case where there is a fourth arguement of description.
        '''
        self.quantity = quantity
        self.unit = unit
        self.name = name
        self.description = description
    
    def print_ingredient(self):
        '''
        Output test.
        '''
        print(self.quantity)
        print(self.unit)
        print(self.name)
        print(self.description)

