# Clinton Garwood
# Pandas Intro Lab (Looking for correlations)

import pandas as pd
import matplotlib.pyplot as plt

# Import Data
df_map = pd.read_csv('correlate_data.csv')

# create a default graph showing all data
# df_map.plot()
# plt.show()

# Create a Scatter Plot
# This demonstrates (pictogram) the relationship between Duration and Calories
# df_map.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
# plt.show()

# Create a Scatter Plot
# This demonstrates (pictogram) the relationship between Duration and MaxPulse
# df_map.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
# plt.show()

# Create a Histogram on Duration
# df_map["Duration"].plot(kind = 'hist')
# plt.show()

# Create a Histogram on Duration
df_map["Calories"].plot(kind = 'hist')
plt.show()