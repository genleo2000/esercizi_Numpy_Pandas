import numpy as np
import pandas as pd

sales = [0, 5, 155, 0, 518, 0, 1827, 616, 317, 325]

# Può ricevere in input anche un array Numpy, purchè sia monodimensionale perchè Pandas e Numpy gestiscono i valori in maniera differente
sales_series = pd.Series(sales, name="Sales") 

print(sales_series)

print(sales_series.values) # restituisce un array Numpy con i valori della Series
print(sales_series.index)
sales_series.index = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # In questo modo si possono modificare gli indici della Series
print(sales_series.name)
print(sales_series.dtype)
print(pd.__version__)

print(sales_series.astype('float')) # Cambia la tipologia degli elementi della Series

another_sales = [0, 5, 7, 9, 12]
indexes = ['coffee','milk','sugar','cake','tea'] # ci possono essere anche indici uguali, in quel caso Pandas resituisce tutti i valori che hanno lo stesso indice
another_series = pd.Series(another_sales, index=indexes, name='Sales Index')
print(another_series)
#print(another_series['coffee'])
#print(another_series['milk':'cake']) # Nel caso di indici alfanumerici, l'ultimo estremo non è esclusivo

print(another_series.iloc[2]) # restituisce il valore in seconda posizione, anche se l'indice è 'sugar'
print(another_series.iloc[2:4]) # restituisce i valori in posizione 2 e 3
print(another_series.iloc[[1,3,4]]) # restituisce i valori in posizione 1, 3 e 4

# A differenza di .loc, .iloc prende in pasto gli indici effettivi della series, non la loro posizione
# Funziona comunque allo stesso modo di .iloc
print(another_series.loc[['milk','cake']]) 
print(another_series[ another_series % 2 == 0])

print(another_series.reset_index()) # Resetta gli indici della Series mantenendo però quelli originari
print(another_series.reset_index(drop=True)) # Resetta gli indici della Series ELIMINANDO però quelli originari