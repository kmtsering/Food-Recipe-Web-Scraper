### Food-Recipe-Web-Scraper


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
