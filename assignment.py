import pandas as pd
import numpy as np

rng = np.random.default_rng()

# Genero un array di valori compresi tra 0 e 100 e li arrotondo a 2 cifre decimali
oil_data = np.round(rng.random(100) * 100, 2) 

print(oil_data)

oil_series = pd.Series(oil_data, name='oil_prices')
print(oil_series)
print(oil_series.name)
print(oil_series.dtype)
print(oil_series.index)

# Genero la media
mean = oil_series.values.mean()
print('La media è',mean)

oil_series_int = oil_series.astype('int')

mean = oil_series_int.values.mean()
print('La media dei numeri interi è',mean)