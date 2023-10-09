'''summary goes here'''
import pandas as pd
import os


PATH = "2023/10/05/cars.csv"
RESOURCES = {
    "https://sparkbyexamples.com/pandas/pandas-get-column-names/#:~:text=You%20can%20get%20the%20column,it%20using%20print()%20statement."
}
df = pd.read_csv(PATH, sep=';')
os.system('clear') # Works on bash, CLS for windows.

'''Grabs the names of all columns and prints each column number name.'''
def get_names(dataframe):
    column_headers = dataframe.columns.values.tolist()
    for i in range(0,len(column_headers)):
        print(f"The name of column number {i+1} is: {column_headers[i]}")

get_names(df)

'''Finding the car with the highest MPG'''
def highest_mpg(dataframe):
    highest = dataframe.idxmax("MPG")
    print(highest)
    return highest