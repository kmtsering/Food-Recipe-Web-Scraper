# import BeautifulSoup, HTMLParser

# Selinium may be more desirable than BeutifulSoup.
# Installation is needed for any libraries mentioned above.

class Recipe():
    '''
    Contains extracted data from site.
    '''
    def __init__(self):
        '''
        Initialization
        '''
        pass

    def ingredient_obejcts():
        '''
        Ingredient information
        '''
        pass

    def directions():
        '''
        Steps/directions from recipe
        '''
        pass

    def etc_info():
        '''
        Holds all other data not relevant for user
        '''
        pass

class IngredientConversion():
    '''
    Measurements from extracted data may need to be converted
    into something into something more applicable to user.
    '''
    def __init__(self):
        '''
        Iniitialization
        '''
        pass

    def amount_f():
        '''
        Pre-converted infomation
        '''
        pass

    def amount_s():
        '''
        Post-converted information
        '''
        pass

    def unit():
        '''
        Holds conversion information for unit to unit
        '''
        pass

    def name():
        '''
        Holds ingredient name for which numbers associated to
        '''
        pass
    
    def amount_converted():
        '''
        Associates pre to post converted amounts
        '''
        pass
    
    def unit_converted():
        '''
        Associates unit names to amounts
        '''
        pass