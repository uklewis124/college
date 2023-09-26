print("start")

# Prerequisites
import pandas as pd
example_csv_path = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

##############
# 1. Series
##############

# 1.1. Creating a series off the top of your head
example_series = pd.Series([1, 2, 3, 4, 5])


# 1.2. Creating a series from a CSV file by selecting a column from the DataFrame
# Parameters:
# - example_csv_path: the path to the CSV file
# Returns:
# - example_series_from_csv: a pandas Series object containing the values from the 'country' column of the CSV file
example_series_from_csv = example_csv_path['country']

##############
# 2. DataFrame
##############

# 2.1. Creating a DataFrame off the top of your head
example_dataframe = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
'''
    Bob             Sue
0   I liked it.     Pretty good.
1   It was awful.   Bland.
'''

