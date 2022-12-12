### Food-Recipe-Web-Scraper

## 1. Summary

This tool will sift through Gimme some Oven pages for recipes and extract only the parts relevant for reproducing it. As a web scraper, it will save web pages into a local file where the relevant details are stored as objects. From there, these objects can be interacted with or processed by this tool to provide the user with data sorting in regards to recipe details as well as categorization. This tool will be able to strip out advertisements, video links, and especially background stories which bear no relevance to the user's intent.


This program is capable of scraping over 1,800 recipes available on https://www.gimmesomeoven.com/all-recipes/. Upon user input of the appropriate link, the program will output a text version of the recipe which would usually appear at the end of the link. This will save the user from excessively scrolling to the information they are looking for. This program is designed to form the basis of larger scale scraping techniques while granting the flexibility to allow higher granularity parsing. At this time, parsing is constrained to the gimmesomeoven.com domain given the complexity of parsing any additional websites.


The BeautifulSoup library from the bs4 module drives the parsing for this web scraper. Python’s built-in urllib is utilized to retrieve a URL input from the which is then turned to a readable html file which is then used by the various extract functions under demo_recipe.

For additional complexity, a means was created to accept user based url input to parse with. This is a massive usability upgrade from the original version which ran off of a manually downloaded webpage that bs4 then parses. Recipes under this domain can oftentimes contain notes that could be helpful. As an additional feature, the program can now provide these notes at the text output if available.

## 2. Overview of the code

Structure wise, demo_recipe.py contains the code to be executed. A flat hierarchy of classes separated by files ensures ease of modification. This would involve Recipe.py, IngredientText.py, and Instruction.py that holds various attributes of the respective object. The list storage approach available on demo_recipe.py allows support for additional features that rely on stored instances of the parsed data.

Code is primarily run through demo_recipe.py. All functions under this file serve to parse and call upon class methods.

Each of the classes below have a dedicated file.

Recipe.py

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

IngredientText.py

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
            Output for user and
            '''
            print(self.text)
      

Instruction.py

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
            
Note.py

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



## 3. Instructions for use

Please begin by loading the code onto your IDE of choice.

To utilize this program, please install BeautifulSoup4 through the following command. If pip installer is not availible to you, please follow pip installation instructions through this link: https://pip.pypa.io/en/stable/installation/
    
    
    pip install beautifulsoup4

After installing BeautifulSoup4, you can now open demo_recipe.py and run the python file. 
From here, you will be promted to enter a URL.
Given that this program is designed specificly for www.gimmesomeoven.com, please be sure to input any recipe link under stated domain.

Copy the url and right click it to the python terminal to paste it.

You will then be provided with a text output of the complete recipe along with any notes at the end. The program resolve at once this output goes through.

Enjoy!

## 4. Sugested future directions

Users can sometimes input a problematic URL outside of the inent of this program. The url_input() can be made more robust by accounting for these error cases.

Users might want to have different units than what is provided on the site. A new feature could involve a more granular parsing of IngredientText through the Pint API. Implementing this tool can become complex since different recipes could contain more than one amount and unit on each ingredient line. 

Support for ingredient substitution could involve pulling a webpage under the domain which could then replace strings of Recipe,IngredientText, Instruction, and Notes. 
