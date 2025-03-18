import numpy as np
import pandas as pd

# dropna() elimina le righe con valori mancanti
# read_csv restituisce un DataFrame
oil = pd.read_csv('assignment/retail/oil.csv').dropna()

oil_array = np.array(oil['dcoilwtico'])

# un oggetto Series può essere inizializzato anche con un array Numpy e può contenere solo una serie di valori monodimensionale
oil_series = pd.Series(oil_array, name='oil_prices')

expression = (oil_series > 90) & (oil_series.index < 10)

print(oil_series.loc[expression])

# Funzioni che restituiscono un booleano per ogni elemento della Series e possono essere dati in pasto a .loc

print(oil_series.ge(90)) # >=
print(oil_series.le(90)) # <=
print(oil_series.gt(90)) # >
print(oil_series.lt(90)) # <
print(oil_series.eq(90)) # ==
print(oil_series.ne(90)) # !=
print(oil_series.between(90, 100)) # tra 90 e 100
print(oil_series.isin([90, 100])) # è 90 o 100


print(oil_series.loc[oil_series.ge(90)])

# FUNZIONI DI ORDINAMENTO

print(oil_series.sort_values()) # Ordina i valori in ordine crescente
print(oil_series.sort_values(ascending=False)) # Ordina i valori in ordine decrescente
print(oil_series.sort_index()) # Ordina gli indici in ordine crescente
print(oil_series.sort_index(ascending=False)) # Ordina gli indici in ordine decrescente

oil_series.sort_values(inplace=True) # con inplace settato a True, la funzione modifica la Series originale

# FUNZIONI ARITMETICHE E OPERAZIONI CON LE STRINGHE

# Aumenta i prezzi del 20% e con il fill_value setta 0 su tutti i valori errati presenti nella Series
oil_series.multiply(1.2, fill_value=0)

age_data = pd.Series(['Adult 25', 'Child 12', 'Adult 64', 'Teen 17', 'Adult 45'])

# Richiamare "str" per utilizzare metodi di manipolazione delle stringhe
# expand trasforma il risultato in un DataFrame
split_data = age_data.str.split(' ', expand=True)

print(split_data[0])

age_groups = pd.Series([
    'Adult', 'Child', 'Adult', 'Teen', 'Adult', 
    'Child', 'Teen', 'Adult', 'Adult', 'Adult'
])

# Calculate the proportion of each age group
age_group_proportions = age_groups.value_counts(normalize=True)

# Output the proportions
print(age_group_proportions)