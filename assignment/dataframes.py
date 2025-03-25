import pandas as pd

transaction = pd.read_csv('retail/transactions.csv')

transaction_copy = transaction.loc[1:, ['store_nbr','transactions']]

values_store_nbr = transaction['store_nbr'].value_counts().sort_index()
unique_store_nbr = transaction['store_nbr'].nunique()
transaction_sum = transaction['transactions'].sum()

print(transaction_sum)