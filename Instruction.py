class Instruction:
    '''
    Holds a single step of the recipe.
    '''

    def __init__(self, order, summary):
        '''
        Instance where there is nothing after <strong> bolding.
        '''
        self.order = str(order)
        self.summary = summary

    def __init__(self, order, summary, description):
        '''
        Instance where all parts of the instruction is fed through.
        '''
        self.order = str(order)
        self.summary = summary
        self.description = description

    def print_instruction(self):
        '''
        Show output.
        Also for diagnostic purposes.
        '''
        print("\n" + (self.order) + ": " + "\033[1m" + self.summary + "\033[0m") # creates new line then prints order with : and bolds the summary
        print(self.description)
