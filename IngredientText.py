class IngredientText:
    '''
    Holds single string of recipe data
    that may be parsed as such.
    '''
    def __init__(self, text):
        '''
        Handles only one argument for recipe text
        '''
        self.text = text

    def print_ingredient_text(self):
        '''
        Output for user and testing.
        '''
        print(self.text)
