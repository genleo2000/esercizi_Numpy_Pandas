import numpy as np
import pandas as pd

list_example = ['COMPLETE',np.nan,np.nan,np.nan,'COMPLETE']
series_example = pd.Series(list_example)

print(series_example)
print(series_example.dropna())
print(series_example.dropna().reset_index(drop=True))

# Sostituisce i valori mancanti con 'INCOMPLETE'
print(series_example.fillna('INCOMPLETE'))

# Numero dei valori mancanti
print(series_example.isna().sum())

# Provided list of ages with missing values and an outlier
age_data = pd.Series([25, np.nan, 30, 45, 110, 37, np.nan, 42, np.nan, 52])

print('Mean = ',age_data.mean())
print('Median = ',age_data.median())

# Prende i valori diversi da 110, altrimenti li sostituisce con np.nan. Il carattere tilde funziona come negazione della condizione
print(age_data.where(~age_data.isin([110]),np.nan)) 

# Prende i valori minori o uguali a 90, altrimenti li sostituisce con np.nan
print(age_data.where(age_data <= 90,np.nan)) 

print(age_data.apply(lambda x: x if x <= 90 else np.nan))
