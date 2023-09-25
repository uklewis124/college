import pandas as pd

# Read the data
df = pd.read_csv('/workspaces/college/2023/09/25/aircrashesFullData.csv')

# Print the first 5 rows
df.head()

# Exploring the data

# Dropping the 'id' column is not necerssary as we
# dont have any type of id column in our dataset

#Combining Day, month and year into a single column
df.insert(0, 'Date', df['Day'].astype(str) + '/' + df['Month'].astype(str) + '/' + df['Year'].astype(str))
print(df.head())

#Listing any values that are year 2000 or later
print(df[df['Year'] >= 2000])