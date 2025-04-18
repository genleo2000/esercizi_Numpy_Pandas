import pandas as pd

data = pd.read_csv('assignment/retail/stores.csv')

print(data.head(20))
data_pivot = data.pivot_table(index='city',columns='store_nbr',values='cluster',aggfunc='sum',margins=True)

print(data_pivot)

print(data.loc[data['city'] == 'Ambato'])