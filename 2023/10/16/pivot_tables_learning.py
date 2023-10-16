import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

x,y = fetch_openml("autos", version=1, as_frame=True, return_X_y=True)
data = x
data['target'] = y

pivot = np.round(pd.pivot_table(data, values='price',
                                index='num-of-doors',
                                columns='fuel-type',
                                aggfunc=np.mean), 2)

print(pivot)

pivot = np.round(pd.pivot_table(data, values='price',
                                index=['make'],
                                columns=['num-of-doors'],
                                aggfunc=np.mean,
                                fill_value=0), 2).plot.barh(figsize=(10,7),
                                                            title='Mean car price by make and number of doors')

print(pivot)

plt.savefig('pivot_table.png')