class Note:
    '''
    Holds and can print out any
    notes that are sometimes provided
    by the recipe.
    '''
    def __init__(self, description):
        '''
        Contains single text line.
        '''
        self.description = description

    def print_note(self):
        '''
        Simple output
        '''
        print("\n" +"NOTE")
        print(self.description)