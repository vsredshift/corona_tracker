# corona_tracker

CoVid-19 Tracker with Python.

# corona_tracker.py
Web scraping program with Beautiful Soup. It scrapes the latest data from the worldmeters website and stores
the relevant data in a pandas dataframe. The data is also exported as a csv file.

# corona.ipynb
A Jupyter notebook. Part One uses the data scraped by the corona_tracker module. 
It contains some functions with examples to perform simple data analysis and comparisons using the current data totals
by region, country and globally. Part Two uses total deaths and total cases data from the John Hopkins University github repository. 
Functions include rolling averages, country-by-country comparisons over time and deaths-to-cases ratios.

# corona_interface.py
Uses the corona_tracker module to get the latest totals. Queries are made verbally. Speech recognition, parsed with regular expressions,
handles the query and returns the response with text-to-audio. This is as yet quite basic and I am working on expanding the regular expressions
patterns and adding more queries. 

This is a work in progress. I intend to create an interactive GUI and/or web application to handle queries and render the graphical data.
Stay posted!
