# The weekly meal planner

This is a tool that generates a weekly meal plan of customized recipes

The recipes themselves are scrapped from the website 'recetasgratis.com' (spanish). For each recipe, it's name, url, category and 5 other features are scrapped. 
After that, the user can set up a selection based on their preferences. The output is a 7X2 table with recipes for the week

This program will send the meal plan via email. For this to work you will need to set up your email information in an environment variable. To do this, in the repository, create a file called ".env". In it, create 3 variables: 

EMAIL="the email account that will send this plan" 

PASSWORD="The password for that email account" 

DESTINATION="the email you want to send this plan to"

