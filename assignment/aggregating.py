import pandas as pd

transaction = pd.read_csv('retail/transactions.csv', parse_dates=['date'])

transaction_sum = transaction.groupby('store_nbr',observed=False)['transactions'].sum().sort_values(ascending=False)
print(transaction_sum.iloc[:10])

# questa modalità non si può utilizzare perchè abbiamo convertito il campo "date" in datetime
#transaction['month'] = transaction['date'].str[5:7]

transaction['month'] = transaction['date'].dt.month
transaction_group = transaction.groupby(['store_nbr','month'], observed=False, as_index=False)[['transactions']].sum()   
print(transaction_group.sort_values(['month','transactions'], ascending=[True,False]).head(20))

transaction_aggr = transaction.groupby(['store_nbr','month'], observed=False)[['transactions']].sum()
print(transaction_aggr.reset_index().head(10))
# Cerca store_nbr=1 e month=3 in base all'ordine di apparizione nel DataFrame
print(transaction_aggr.loc[(1,3)])

print('\n\n')
transaction_aggr = transaction.groupby(['store_nbr','month'], observed=False).agg({'transactions': ['sum','mean']})
print(transaction_aggr)
