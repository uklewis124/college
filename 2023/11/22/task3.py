import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('2023/11/22/Task3_data.csv')

# Defining functions to find out how many flights per month
def flights_per_month():
    global df
    month_series = df['Month']
    print(month_series)
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
    os.system('clear')
    for months in range(1, 13):
        print("Months: ", months)
        print(month_series[months])
        print('Month: ', month_names[months], '||', 'Flights: ', len(month_series['Month'][months]))

flights_per_month()