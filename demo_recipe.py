from urllib.request import urlopen, Request             # library for pulling html by url
from bs4 import BeautifulSoup                           # html parsing tool
from Recipe import Recipe
from IngredientText import IngredientText
from Instruction import Instruction                     # syntax is file then class
from Note import Note

def url_input():
    '''
    Accepts user provided url
    to create html file for
    parsing.
    '''
    user_url = input("Please input recipe a link from https://www.gimmesomeoven.com: ")
    user_url
    print("\n")
    url_header = Request(user_url, headers={'User-Agent': 'XYZ/3.0'})   # sets headers to prevent site 403 error

    url_html = urlopen(url_header, timeout=1).read()                    # retrieves link with 1 sec timeout to prevent site security blocking

    return BeautifulSoup(url_html, features="html.parser")

header_list = []       # stores instances of Recipe 
def extract_header(soup_obj):
    '''
    Extracts header information from html
    and returns new Recipe object.
    '''

    name = soup_obj.body.find('h2', attrs={'class' : 'tasty-recipes-title'}).text
    yields = soup_obj.body.find('span', attrs={'class' : 'tasty-recipes-yield'}).text
    total_duration = soup_obj.body.find('span', attrs={'class' : 'tasty-recipes-total-time'}).text


    header_list.append(Recipe(name, yields, total_duration))            # adds Recipe intance to list
    return header_list[0]                                               # returns first instance of list


ingredient_list = []    # stores instances of IngredientText

def extract_ingredients(soup_obj):
    '''
    Extracts all ingredients from HTML
    and put it into recipe object.
    '''
    ingredient_parent_node = soup_obj.find('div', {'class' : 'tasty-recipes-ingredients-body'})    # narrows scope to ingredients body
    ingredient_parent_subnode = ingredient_parent_node.findChild()                                 # steps down one node from parent 
    ingredient_children= ingredient_parent_subnode.findChildren("li", recursive=False)             # scopes into each ingredient and groups them as a variable
    


    for child in ingredient_children:
        ingredient = IngredientText(child.text)         # initializes IngredientText with single text line of HTML text
        ingredient_list.append(ingredient)              # adds this instance of IngredientText to list
        ingredient.print_ingredient_text()              # calls IngredientText print method

instructions_list = []            # stores instances of Instruction

def extract_instructions(soup_obj):
    '''
    Extracts instructions from HTML
    and put it into recipe object
    '''
    instructions_block = soup_obj.find('ol')                                        # narrows scope to instructions tree
    instructions_children = instructions_block.findChildren("li", recursive=False)  # furthers narrows down to individual instructions
    


    order = 0           # tracks step number

    for child in instructions_children:             # separates each child as its own workable instance
        summary = child.find(['strong']).text       # finds bolded instruction text
        description = child.find('span').text       # finds instruction description

        order += 1      # increments step number for next loop

        instruction = Instruction(order, summary, description)    # places variables into class
        instructions_list.append(instruction)                     # adds Instruction instance to list
        instruction.print_instruction()                           # uses Instruction method to print

notes_list = []             # stores instances of Note

def extract_notes(soup_obj):
    '''
    Parses notes for ingredient if any are provided.
    '''
    notes_block = soup_obj.find('div', {'class' : 'tasty-recipes-notes-body'}) # finds any existing notes as a larger body

    if notes_block==None:           # checks to see if notes for recipe exists
        return None                 # prevents error by halting further parse requests
    else:
        notes_children = notes_block.findChildren("p", recursive=False)     # steps 1 increment in tree


        for child in notes_children:
            note = Note(child.text) # single text line for a note being fed into class
            notes_list.append(note) # adds to list an object
            note.print_note()       # calls Note print method



def main():
    '''
    Executes all functions relevant to program
    '''
    soup_obj = url_input()                  # variable will be used for all parsing functions
    soup_obj                                # executes input prompt and returns parseable html object
    
    
    # parses elements of interest
    my_recipe = extract_header(soup_obj)
    my_recipe.print_header()                # prints out header

    extract_ingredients(soup_obj)
    
    extract_instructions(soup_obj)
    
    extract_notes(soup_obj)

main()