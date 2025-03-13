import pandas as pd
import numpy as np

# Leggo i dati da un file csv
oil = pd.read_csv('retail/oil.csv').dropna()

# eseguo la iloc per selezionare le righe da 1000 a 1100
oil_array = np.array(oil['dcoilwtico'].iloc[1000:1100])
print(oil_array)

oil_series = pd.Series(oil_array, name='oil_prices')
print(oil_series.name)
print(oil_series.dtype)
print(oil_series.index)

# Genero la media
mean = oil_series.values.mean()
print('La media è',mean)

oil_series_int = oil_series.astype('int')

mean = oil_series_int.values.mean()
print('La media dei numeri interi è',mean)

dates = np.array(oil['date'].iloc[1000:1100])
oil_series.index = dates

print(oil_series.iloc[:10].mean())
print(oil_series.iloc[-10:].mean())
