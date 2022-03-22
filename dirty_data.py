# Clinton Garwood
# Pandas Intro Lab (Working with dirty_data.csv)

import pandas as pd
# Read the dirtydata.csv file into a pandas dataframe from file
df_d = pd.read_csv('dirtydata.csv') # for dropping values
df_f = pd.read_csv('dirtydata.csv') # for filling values

# when we view the data using df.info we see there are null values in the set
df_d.info()
# 1 date is missing, and two calories are missing

# Pandas has an option to allow us to drop all rows which have any null value
df_d.dropna(inplace = True)
print(df_d.to_string())

# Alternately we can drop a row with a void in a single column
# df_d.dropna(subset=['Date'], inplace = True)  # drop rows with null in Date
# df_d.dropna(subset=['Calories'], inplace = True)  # drop rows with null in Calories

# running df.info() again we see 29 values of each kind = no null values
df_d.info()

# the other way we could operate is to specify a value to replace the voids
# df_f.fillna(130, inplace = True) # This method simply puts 130 in all void spots
# df_f["Calories"].fillna(130, inplace = True) # this method only fill 'Calories" voids
# This method fills in the 'average' for void places
# cal_mean = df_f["Calories"].mean() # is sum/total_count
# cal_med = df["Calories"].median() # median is center most value
# cal_mode = df["Calories"].mode()[0] # mode is most frequent value
# df_f["Calories"].fillna(x, inplace = True)

# Manually changing data in the data frame
# in row 7 the duration of the workout is 450 minutes, but should be 45.
df_d.loc[7, 'Duration'] = 45

# Alternately we can use a loop to find outliners, and set a maximum
# value if/when they are found
for x in df_d.index:
  if df_d.loc[x, "Duration"] > 120:
    df_d.loc[x, "Duration"] = 120
  # df_d.dropna(subset=['Date'], inplace = True)  # drop rows with null in Date

# Another option for the loop loop is to remove rows with  outliners
for x in df_d.index:
  if df_d.loc[x, "Duration"] > 120:
    df_d.drop(x, inplace=True)

# Sometimes duplicated data exists.
print("we can call df.duplicated() to discover duplicate rows")
print(df_d.duplicated())

print("To drop duplicate rows use df.drop_duplicates(inplace = True) ")
df_d.drop_duplicates(inplace = True)
print(df_d.duplicated())
