# Clinton Garwood
# Pandas Intro Lab (Sum of Column based on Condition from csv)

import pandas as pd
# this call assumes each column of data has a column name
df_sum = pd.read_csv('data.csv')
# this call indicates there are no column names
#df_sum = pd.read_csv('data.csv', header=None)
print(df_sum.to_string())

# print(df_sum.info())

print(df_sum.axes)

print("\n The sum of Duration is", df_sum['Duration'].sum())
print("The sum of Calories is", df_sum['Calories'].sum())
#print("The sum of Calories > 200 is", df_sum['Calories'].sum())
print("The sum of Calories > 200 is", df_sum.loc[df_sum['Calories'] > 200].sum())

# https://www.statology.org/pandas-sum-column-with-condition/

# df_sum.loc[df_sum['Duration'] == 'A', 'points'].sum()
