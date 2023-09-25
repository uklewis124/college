import pandas as pd

df = pd.read_csv('movie_budgets', index_col='id')
print(df.head())