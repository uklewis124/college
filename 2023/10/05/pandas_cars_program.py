'''summary goes here'''
import pandas as pd
import numpy as np


PATH = "2023/10/05/cars.csv"
RESOURCES = {
    "https://sparkbyexamples.com/pandas/pandas-get-column-names/#:~:text=You%20can%20get%20the%20column,it%20using%20print()%20statement."
}
df = pd.read_csv(PATH, sep=';')

def get_names(dataframe):
    column_headers = dataframe.columns.values.tolist()
    for i in range(0,len(column_headers)):
        print(f"The name of column number {i+1} is: {column_headers[i]}")

get_names(df)
