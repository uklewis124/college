import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2023/11/22/Task3_data.csv')

# Defining functions to find out how many flights per month
def flights_per_month():
    global df
    month_series = df['Month']
    month_names = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    for months in range(1, 13):
        print("Months: ", months)
        print('Month: ', month_names[months], '||', 'Flights: ', month_series.value_counts().iloc[months])

flights_per_month()