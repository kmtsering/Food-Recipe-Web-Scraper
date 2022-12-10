
from bs4 import BeautifulSoup
import Recipe
import Instruction

def extract_header(soup_obj):
    '''
    Extracts header information from html
    and returns new Recipe object.
    '''

    name = soup_obj.body.find('h2', attrs={'class' : 'tasty-recipes-title'}).text
    yields = soup_obj.body.find('span', attrs={'class' : 'tasty-recipes-yield'}).text
    total_duration = soup_obj.body.find('span', attrs={'class' : 'tasty-recipes-total-time'}).text
    
    return Recipe.Recipe(name, yields, total_duration)

def extract_ingredients(soup_obj):
    '''
    Extracts all ingredients from HTML
    and put it into recipe object.
    '''
    ingredient_parent_node = soup_obj.find_('div', {'class' : 'tasty-recipes-ingredients-body'})
    ingredient_children= ingredient_parent_node.findChildren("li", recursive=False)
    
    for child in ingredient_children:
        parts = child.findChildren("span", recusive=False)
        for part in parts:
            print(part.text)

def extract_instructions(soup_obj):
    '''
    Extracts instructions from HTML
    and put it into recipe object
    '''
    instructions_block = soup_obj.find('ol')
    instructions_children = instructions_block.findChildren("li", recursive=False)

    order = 0

    for child in instructions_children:
        summary = child.find(['strong']).text
        description = child.find('span').text
        
        Instruction.Instruction(order, summary, description)

        order += 1

        print(order)
        print(summary)
        print(description)

    #order = soup_obj.
    #summary = 
    #description =



def main():
    # open .html file from local drive
    file = open("HTML Files\Bacon Brussels Sprouts with Hot Honey - Gimme Some Oven.html", encoding='utf-8')

    # create BeautfiulSoup object from that file 
    # NOTE: features parameter required to get rid of library warning in output
    soup_obj = BeautifulSoup(file, features="html.parser")

    # finds elements of interest
    my_recipe = extract_header(soup_obj)
    my_recipe.print_header()

    extract_instructions(soup_obj)

    extract_ingredients(soup_obj)
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