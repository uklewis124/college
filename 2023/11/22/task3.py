import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('2023/11/22/Task3_data.csv')

# Defining functions to find out how many flights per month
def flights_per_month():
    global df
    month_series = df['Month'].groupby(df['Month'], sort=False).count()
    print(month_series)

    print('The month with the most flights is: ', month_series.idxmax())
    fig = plt.figure()
    plt.figsize=(30, 30)
    plt.xticks(rotation=90)
    plt.xlabel('Month')
    plt.ylabel('Number of flights')
    plt.plot(month_series)
    plt.savefig('2023/11/22/output.png')


flights_per_month()