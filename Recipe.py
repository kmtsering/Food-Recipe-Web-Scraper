import Ingredient       # access ingredient class to put ingredient objects into recipe
import Instruction      # access instruction class to put directions into recipe
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
        self.instruction_list = []

    def create_ingredient_entry(self, quantity, unit, name, description):
        '''
        Creates one Ingredient object 
        and appends to ingredient_list
        '''
        self.ingredient_list.append(Ingredient.Ingredient(quantity, unit, name, description))

    def print_header(self):
        '''
        Prints out name, yields, and total time.
        '''
        print(self.name)
        print(self.yields)
        print(self.total_time + "\n")
    
    def create_instruction_entry(self, order, summary, description):
        '''
        Prints out directions in step, summary, and descripton.
        '''
        self.instruction_list.append(Instruction.Instruction(order, summary, description))



# import html.parser

    

