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
        '''
        self.order = str(order)
        self.summary = "\033[1m" + summary + "\033[0m"
        self.description = description + "\n"

    def print_instruction(self):
        '''
        Show output
        '''
        print(self.order)
        print(self.summary)
        print(self.description)
