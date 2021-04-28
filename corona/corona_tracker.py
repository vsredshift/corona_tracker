import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

""" Get the latest data on Covid19 from the worldmeters website.
    The relevant data is scraped and stored in a dictionary.
    The dictionary is then converted to a pandas DataFrame
    and exported to a csv file. """

url = 'https://www.worldometers.info/coronavirus/'
source = requests.get(url).text
soup = BS(source, 'lxml')

country_list = []
for table_row in soup.select('table.main_table_countries tr'):
    if table_row.find_all('a', {'class': 'mt_a'}):
        cell = table_row.find_all('td')

        country_name = cell[1].text.strip()

        total_cases = int(cell[2].text.strip().replace(',', ''))

        total_deaths = cell[4].text.strip().replace(',', '')

        total_recovered = cell[6].text.strip().replace(',', '')

        active_cases = cell[8].text.strip().replace(',', '')
        serious_cases = cell[9].text.strip().replace(',', '')

        cases_per_million = cell[10].text.strip().replace(',', '')
        deaths_per_million = cell[11].text.strip().replace(',', '')

        continent = cell[15].text.strip()
        population = cell[14].text.strip().replace(',', '')
#
        country = {
            'Country': country_name,
            'Total Cases': total_cases,
            'Total Deaths': total_deaths,
            'Total Recovered': total_recovered,
            'Active Cases': active_cases,
            'Critical Cases': serious_cases,
            'Total Cases per Million': cases_per_million,
            'Total Deaths per Million': deaths_per_million,
            'Continent': continent,
            'Population': population
        }
        country_list.append(country)

countries = pd.DataFrame(country_list)
# Drop duplicates by country name
countries.drop_duplicates(subset=['Country'], inplace=True)
# Export data to csv


countries.to_csv('countries.csv')
print("Update complete")