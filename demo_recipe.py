
from urllib.request import urlopen, Request                          # library for pulling html by url
from bs4 import BeautifulSoup                           # html parsing tool
from Recipe import Recipe
from IngredientText import IngredientText
from Instruction import Instruction                     # syntax is file then class

def url_input():
    '''
    Accepts user provided url
    to create html file for
    parsing.
    '''
    user_url = input("Please input recipe a link from https://www.gimmesomeoven.com: ")
    user_url
    print("\n")
    # test_url = 'https://www.gimmesomeoven.com/bacon-brussels-sprouts-with-hot-honey/'
    url_header = Request(user_url, headers={'User-Agent': 'XYZ/3.0'})   # sets headers to prevent site 403 error

    url_html = urlopen(url_header, timeout=1).read()                    # retrieves link with 1 sec timeout to prevent site security blocking

    return BeautifulSoup(url_html, features="html.parser")

    
def extract_header(soup_obj):
    '''
    Extracts header information from html
    and returns new Recipe object.
    '''

    name = soup_obj.body.find('h2', attrs={'class' : 'tasty-recipes-title'}).text
    yields = soup_obj.body.find('span', attrs={'class' : 'tasty-recipes-yield'}).text
    total_duration = soup_obj.body.find('span', attrs={'class' : 'tasty-recipes-total-time'}).text

    header_list = []                                                    # contains instances of Recipe
    header_list.append(Recipe(name, yields, total_duration))            # adds Recipe intance to list
    return header_list[0]                                               # returns first instance of list


def extract_ingredients(soup_obj):
    '''
    Extracts all ingredients from HTML
    and put it into recipe object.
    '''
    ingredient_parent_node = soup_obj.find('div', {'class' : 'tasty-recipes-ingredients-body'})    # narrows scope to ingredients body
    ingredient_parent_subnode = ingredient_parent_node.findChild()                                 # steps down one node from parent 
    ingredient_children= ingredient_parent_subnode.findChildren("li", recursive=False)             # scopes into each ingredient and groups them as a variable
    
    ingredient_list = []    # move outside of function to make it a global variable

    for child in ingredient_children:
        ingredient = IngredientText(child.text)         # initializes IngredientText with single text line of HTML text
        ingredient_list.append(ingredient)              # adds this instance of IngredientText to list
        ingredient.print_ingredient_text()              # calls IngredientText print method
    
    # following docstring contains incomplete version of high granularity parser
    """ ingredient_parent_node = soup_obj.find_('div', {'class' : 'tasty-recipes-ingredients-body'})
    ingredient_children= ingredient_parent_node.findChildren("li", recursive=False)
    
    for child in ingredient_children:
        parts = child.findChildren("span", recusive=False)
        for part in parts:
            print(part.text) """

def extract_instructions(soup_obj):
    '''
    Extracts instructions from HTML
    and put it into recipe object
    '''
    instructions_block = soup_obj.find('ol')                                        # narrows scope to instructions tree
    instructions_children = instructions_block.findChildren("li", recursive=False)  # furthers narrows down to individual instructions
    
    instructions_list = []            # move outside of function to make it a global variable

    order = 0           # tracks step number

    for child in instructions_children:             # separates each child as its own workable instance
        summary = child.find(['strong']).text       # finds bolded instruction text
        description = child.find('span').text       # finds instruction description

        order += 1      # increments step number for next loop

        instruction = Instruction(order, summary, description)    # places variables into class
        instructions_list.append(instruction)                     # adds Instruction instance to list
        instruction.print_instruction()                           # uses Instruction method to print

    instructions_list[0].print_instruction() # this is to test if the list storing works


def main():
    """ # open .html file from local drive
    file = open("HTML Files\Bacon Brussels Sprouts with Hot Honey - Gimme Some Oven.html", encoding='utf-8')

    # create BeautfiulSoup object from that file 
    # NOTE: features parameter required to get rid of library warning in output
    soup_obj = BeautifulSoup(file, features="html.parser") """

    # user_url = input("Please input recipe a link from https://www.gimmesomeoven.com: ")
    # user_url
    # # test_url = 'https://www.gimmesomeoven.com/bacon-brussels-sprouts-with-hot-honey/'
    # url_header = Request(user_url, headers={'User-Agent': 'XYZ/3.0'})   # sets headers to prevent site 403 error

    # url_html = urlopen(url_header, timeout=1).read()                    # retrieves link with 1 sec timeout to prevent site security blocking

    # soup_obj = BeautifulSoup(url_html, features="html.parser")                                
    
    soup_obj = url_input()                  # variable will be used for all parsing functions
    soup_obj                                # executes input prompt and returns parseable html object
    
    
    # parses elements of interest
    my_recipe = extract_header(soup_obj)
    my_recipe.print_header()

    extract_ingredients(soup_obj)
    
    extract_instructions(soup_obj)
    
    
    '''
    # print elements of interest
    print(name)
    print("Total time: ",total_duration)
    print(yields)
    '''
    # create Recipe object with elements of itnerest
    #rec = Recipe.Recipe()

    #rec.print_header()
main()