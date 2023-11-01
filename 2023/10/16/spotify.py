import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.datasets import fetch_openml

parent_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))
print(parent_folder)
parent_csv = os.path.join(parent_folder, '/res/spotify-2023.csv')
df = pd.read_csv('/workspaces/college/2023/10/16/res/spotify-2023.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

data = df.nlargest(10, 'streams').sort_values(by='streams', ascending=True)

pivot = np.round(pd.pivot_table(data, values='streams',
                                index='artist(s)_name',
                                aggfunc=np.sum,
                                fill_value=0), 2).plot.barh(figsize=(10,7),
                                                            title='Streams by Artists (Top 10)')

print(plt.show())

plt.savefig('2023/10/16/output/streams_x_artist_top_10.png')

data = df.nsmallest(10, 'streams').sort_values(by='streams', ascending=False)

pivot = np.round(pd.pivot_table(data, values='streams',
                                index='artist(s)_name',
                                aggfunc=np.sum,
                                fill_value=0), 2).plot.barh(figsize=(10,7),
                                                            title='Streams by Artists (Bottom 10)')

plt.savefig('2023/10/16/output/streams_x_artist_bottom_10.png')