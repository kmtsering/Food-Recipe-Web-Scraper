
from bs4 import BeautifulSoup
import Recipe


def main():
    # open .html file from local drive
    file = open("Bacon Brussels Sprouts with Hot Honey - Gimme Some Oven.html", encoding='utf-8')

    # create BeautfiulSoup object from that file 
    # NOTE: features parameter required to get rid of library warning in output
    soup_obj = BeautifulSoup(file, features="html.parser")

    # finds elements of interest
    name = soup_obj.body.find('h2', attrs={'class' : 'tasty-recipes-title'}).text
    total_duration = soup_obj.body.find('span', attrs={'class' : 'tasty-recipes-total-time'}).text
    yields = soup_obj.body.find('span', attrs={'class' : 'tasty-recipes-yield'}).text


    # print elements of interest
    print(name)
    print("Total time: ",total_duration)
    print(yields)

    # create Recipe object with elements of itnerest
    #rec = Recipe.Recipe()

    #rec.print_header()
main()