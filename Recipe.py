import Ingredient       # access ingredient class to put ingredient objects into recipe

class Recipe:
    '''
    Parent class for all desired data.
    '''
    def __init__(self, name, yields, total_time):
        '''
        Initialization for primitive data on the recipe header.
        '''
        self.name = name                    # self referencing to accept input
        self.yields = yields
        self.total_time = total_time
        self.ingredient_list = []
        
    def print_header(self):
        '''
        Prints out name yields and total time.
        '''
        print(self.name)
        print(self.yields)
        print(self.total_time)


# import html.parser

    

