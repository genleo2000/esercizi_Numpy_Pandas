import pandas as pd

transaction = pd.read_csv('assignment/retail/transactions.csv')
print(transaction)
print(transaction.shape)

# Numero delle righe
print(transaction.shape[0])

print(transaction.head(15))
print(transaction.sample(15))

print(transaction.info())

# Restituisce un DataFrame con le statistiche di base
print(transaction.describe())

print(transaction.isna().sum())
