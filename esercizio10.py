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

# Restituisce quanti valori nulli ci sono
print(transaction.isna().sum())

# Richiamiamo una colonna del DataFrame, la funzione restituisce una Serie
print(transaction['store_nbr'])

# Restituisce un DataFrame (anche se avessimo indicato una sola colonna, per via delle parentesi quadre)
# Le colonne saranno indicate nell'ordine in cui appaiono nella loc
print(transaction.loc[:5, ['store_nbr', 'date']])

print(transaction.drop(labels='store_nbr', axis=1).head())
print(transaction.drop(range(5), axis=0).reset_index().head())
print(transaction.shape)
print(transaction.drop_duplicates(keep='last').head())
print(transaction.drop_duplicates(keep='last').reset_index(drop=True).head())
