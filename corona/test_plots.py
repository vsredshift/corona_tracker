from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


cases = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
deaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

cases_data = pd.read_csv(cases)
deaths_data = pd.read_csv(deaths)


# Drop duplicates
cases_data.drop_duplicates(subset='Country/Region', keep='last', inplace=True)
deaths_data.drop_duplicates(subset='Country/Region', keep='last', inplace=True)

# Reset index to country names
cases_data.set_index('Country/Region', inplace=True)
deaths_data.set_index('Country/Region', inplace=True)

# Drop irrelevant columns
cases_data.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)
deaths_data.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)


countries = ['Sweden', 'Norway', 'Denmark']
new_data = deaths_data[deaths_data.index.isin(countries)].astype(float)
plotting_data = new_data.T
plotting_data.index = pd.to_datetime(plotting_data.index)

plt.style.use('fivethirtyeight')

# fig, ax1 = plt.subplots() 


# ax1.plot(plotting_data['Sweden'].loc['2021-2-1':], color='lightblue', linestyle='dotted')

# ax2 = ax1.twin()

# ax2.plot(plotting_data['Denmark'].loc['2021-2-1':], color='red', linestyle='dotted')

# fig.autofmt_xdate()
# fig.tight_layout()
# plt.show()
# # %%

plotting_data['daily'] = plotting_data['Sweden'].diff()

y = plotting_data['daily']
x = np.arange(len(y))
plt.xticks(ticks=plotting_data.index.month, labels=plotting_data.index)
plt.bar(x, y)
plt.show()
