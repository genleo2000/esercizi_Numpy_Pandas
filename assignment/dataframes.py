import pandas as pd

transaction = pd.read_csv('retail/transactions.csv')

transaction_copy = transaction.loc[1:, ['store_nbr','transactions']]

values_store_nbr = transaction['store_nbr'].value_counts().sort_index()
unique_store_nbr = transaction['store_nbr'].nunique()
transaction_sum = transaction['transactions'].sum()

value_null = transaction.isna().sum()

print(transaction.head(20)) 
print(value_null['date'])

transaction_data = transaction.loc[transaction['transactions'] > 2000]
val_data = transaction_data['store_nbr'].count()
val_tot = transaction['store_nbr'].count()
val_perc = (val_data / val_tot) * 100
print(val_perc)

mask = (transaction['store_nbr'] == 25) & (transaction['transactions'] > 2000)
transaction_data = transaction.loc[mask]
val_data = transaction_data['store_nbr'].count()
print(val_data)

# mettere tra parentesi tonde il risultato della loc con il count e selezionare l'indice 2 che indica il count totale della colonna 2
val_tot = (transaction.loc[transaction['store_nbr'] == 25].count()).iloc[2]
print(val_tot)

val_perc = (val_data / val_tot) * 100
print(val_perc)