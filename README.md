# The weekly meal planner

This is a tool that generates a weekly meal plan of customized recipes

The tool starts with a scraping of the recetasgratis.net using BeautifulSoup. The result is a dataframe saved to csv format containing over 10.000 recipes with 9 columns. 

Next, the program uses a pre-defined set of customized preferences (specified in the separate JSON file) to filter the table. 14 meals are selected for each week, 7 lunches and 7 dinners, following the customized preferences that they user defined for each day. 

The resulting selection is then compiled into the body of an email in HTML format. This email is then distributed to a mailing list which was separately defined using environment variables and called into the script. 

Finally, the script was given a schedule to make it run automatically on a weekly basis, and it was uploaded to the cloud (DigitalOcean) so that it would run autonomously.  
