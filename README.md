# Food-Recipe-Web-Scraper

Various recipe sites have the tendancy of providing superflous information before showing the actual ingredients and procedures that the user intended 

1. This project will be done by Kalsang Tsering

2. An overview of the project similar in scope and length to the example projects listed below.

Create a bot to automatically retweet tweets with a particular hashtag or follow users who tweet with a particular hashtag, reply to users tweeting a certain phrase at it with a randomized selection from a list of potential responses, and periodically post tweets (for example, it might tweet a new picture of your cat every 6 hours). You should be able to update the  hashtags your Twitter bot is interested in, change the trigger phrase that the bot will respond to, add items to or remove items from the list of potential responses, and add tweets to or remove items from the tweet queue. Your Twitter bot should also be able to export a summary of its activity to a file. The summary file might contain information like the number of tweets it has responded to, the number of accounts it's following, a random sampling of the tweets it's responded to or retweeted, and a list of the tweets it has made. 

This tool will sift through foodnetwork pages for recipes and extract only the parts relevant for reproducing it. As a web scraper, it will save web pages into a local file where the relevant details are stored as objects. From there, these objects can be intereacted with or processed by this tool to provide the user with data sorting in regards to recipe details as well as categorization. This tool will be able to strip out advertisments, video links, and especially background stories which bear no relevance to the user's intent. 

3. A short description of the structure of your project. 
How many classes will you write? 
Recipe: save_to_file()
    string recipe_name
    list ingedient_objects
    list directions
    list etc_info
Ingredient: convert_to_mass()
    float amount_f
    string amount_s
    string unit
    string name
    float amount_converted
    string unit_converted
    
  
What the methods be for each class? (You can change this if it turns out a better structure would work better once you start writing code and you decide to refactor. Just try to come up with a reasonable one for the proposal.)

4. What libraries and tools will you need to learn to use?
"How to read HTML files"
"Import html for python?"
"google the small steps"

5. Identify the 
highest-priority features, :
the medium-priority features, :
and the lowest-priority features for your project:

For each feature you identified, make an issue (button on the front page of your repository to the right of the button for "code"). Make one additional issue for writing the skeleton or outline of your code. 
