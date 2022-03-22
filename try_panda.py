# Clinton Garwood
# Pandas Intro Lab (Working with data.csv)

import pandas as pd
# this call assumes each column of data has a column name
df_s = pd.read_csv('simple_data.csv')
# this call indicates there are no column names
df = pd.read_csv('data.csv', header=None)
# print(df.to_string())

# Quick look at data (head and tail)
# notice that even though our columns dont have names, and our
# rows don't have titles, each column and row is labeled starts with 0
print("\nHeads")
print(df.head(2))  # this will show top two rows
print("\nTails")
print(df.tail(2))  # this will show last two rows

# A Row of Data in Pandas df
# First (zeroith) piece of data (column zero) for each row
print("\nThis is the first row of [0] data") # each item printed on its own line
print(df.loc[0])
print("\nThis is fifth row of data [4] data") # each item printed on its own line
print(df.loc[4])

# Panda Series
# First two rows of data (column zero and 1) - full row.
# The result has
print("\nFirst two rows of data [0] and [1]")
print(df.loc[[0, 0]])

# First piece of data (column zero) in the first (zeroith) row
row_one_one = df.loc[0][0]
print(row_one_one)

print("\ndf.index")
print(df.index)

print("\ndf.columns")
print(df.columns)

print("\ndf.describe()")
print(df.describe())

print("\n get column [1]")
print(df[1])

# The .iloc attribute is an access method that can take as valid input:
#  An integer e.g. 5.
#  A list or array of integers [1, 2, 22].
#  A slice object with ints 1:5.
#  A boolean array.
#  A callable

print("\ndf.iloc[0:] prints first row without row index labels")
df_row1 = df.iloc[0:1]
print(df_row1.to_string(index=False))

print("\ndf.iloc[162:] prints last two rows")
print(df.iloc[168:])


# reveals number of rows (170) rows and columns (4):
print("\ndf.info prints either the data, or a summary of the data")
# print(df.info) # This call prints the data.
df.info() # this call prints a summary of the data

