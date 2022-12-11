from Ingredient import Ingredient       # access ingredient class to put ingredient objects into recipe
from Instruction import Instruction      # access instruction class to put directions into recipe
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

    def print_header(self):
        '''
        Prints out name, yields, and total time.
        '''
        print(self.name)
        print(self.yields)
        print(self.total_time + "\n")
    
    def create_ingredient_entry_text(self, ingredient_text):
        '''
        Appends to ingredient_list
        for text only case.
        '''
        self.ingredient_list.append(Ingredient.Ingredient(ingredient_text))

    def print_ingredients_text(self):
        '''
        Prints out each Ingredient text
        '''
        for ingredient_list in ingredient_list:
            Ingredient.print_ingredient_text()


    def create_ingredient_entry(self, quantity, unit, name, description):
        '''
        Creates one Ingredient object 
        and appends to ingredient_list
        '''
        self.ingredient_list.append(Ingredient.Ingredient(quantity, unit, name, description))

    def create_instruction_entry(self, order, summary, description):
        '''
        Creates directions in step, summary, and descripton
        and appends to instruction_list
        '''
        self.instruction_list.append(Instruction(order, summary, description))
        
        """ instruction = Instruction(order, summary, description)
        self.instruction_list.append(instruction) """

    def print_instructions(self):
        '''
        Prints out each Instruction
        '''
        for self.instruction_list in self.instruction_list:
            Instruction.print_instruction()


# import html.parser

    

