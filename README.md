### Food-Recipe-Web-Scraper

## 1. Summary

This tool will sift through Gimme some Oven pages for recipes and extract only the parts relevant for reproducing it. As a web scraper, it will save web pages into a local file where the relevant details are stored as objects. From there, these objects can be interacted with or processed by this tool to provide the user with data sorting in regards to recipe details as well as categorization. This tool will be able to strip out advertisements, video links, and especially background stories which bear no relevance to the user's intent.


This program is capable of scraping over 1,800 recipes available on https://www.gimmesomeoven.com/all-recipes/. Upon user input of the appropriate link, the program will output a text version of the recipe which would usually appear at the end of the link. This will save the user from excessively scrolling to the information they are looking for. This program is designed to form the basis of larger scale scraping techniques while granting the flexibility to allow higher granularity parsing. At this time, parsing is constrained to the gimmesomeoven.com domain given the complexity of parsing any additional websites.


The BeautifulSoup library from the bs4 module drives the parsing for this web scraper. Python’s built-in urllib is utilized to retrieve a URL input from the which is then turned to a readable html file which is then used by the various extract functions under demo_recipe.


## 2. Overview of the code

Describe each class and its attributes and methods. How do the classes 
relate to each other? Do any inherit from each other? Are there any 
classes that contain objects of other classes in their attributes?

Structure wise, demo_recipe.py contains the code to be executed. A flat heiarchy of classes separated by files ensures ease of modification. This would involve Recipe.py, IngredientText.py, and Instruction.py that holds various attributes of the respective object. The list storage approach availible on demo_recipe.py allows support for additional features that rely on stored instances of the parsed data. 

## 3. Instructions for use

Assume you have a user (me) who wants to download your code and try out 
your program. Write some sample code and instructions on how to use your
 program that somebody who is almost totally unfamiliar with your 
project would be able to follow.


## 4. Sugested future directions

Say that someone sees your project and decides that it's very cool and 
they want to develop it further. What would you suggest that they work 
on next? Suggest at least 2 features that you would suggest future 
programmers develop. 

## 1. Team

This project will be done by Kalsang Tsering

## 2. Overview
This tool will sift through foodnetwork pages for recipes and extract only the parts relevant for reproducing it. As a web scraper, it will save web pages into a local file where the relevant details are stored as objects. From there, these objects can be intereacted with or processed by this tool to provide the user with data sorting in regards to recipe details as well as categorization. This tool will be able to strip out advertisments, video links, and especially background stories which bear no relevance to the user's intent. 

## 3. Structure

There will be at least two classes needed at this time. Recipe will be the parent while Ingredient is a child.

class Recipe: save_to_file()

    string recipe_name
    
    list ingedient_objects
    
    list directions
    
    list etc_info
    
class Ingredient: convert_to_mass()


    float amount_f
    
    string amount_s
    
    string unit
    
    string name
    
    float amount_converted
    
    string unit_converted
    
  

## 4. Libraries/Tools

What libraries and tools will you need to learn to use?

Library BeautifulSoup: Multipurpose web scraping library capable of doanloading, outputting and parsing HTML files under python.

Library HTMLParser: The basis for parsing text file formatted in HTML. Another option for parsing.

## 5. Priority of Features

Highest-priority: HTML Extraction, File Save

Medium-priority: Processing HTML data, Presenting to User

Lowest-priority: Fine Tuning for Readability
