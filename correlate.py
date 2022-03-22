# Clinton Garwood
# Pandas Intro Lab (Looking for correlations)

import pandas as pd
# Read the dirtydata.csv file into a pandas dataframe from file
df_corr = pd.read_csv('correlate_data.csv') # for dropping values

print("Does one column in the data have a correlation to another?")
print("use the function call df.corr() to generate a summary.")
print(df_corr.corr())

print("1.000~ is a perfect correlation, and less perfect goes down from there.")
print("negative correlations cand also exist")
print("and 60% or better is basic standard for Yes, a correlation exists.")