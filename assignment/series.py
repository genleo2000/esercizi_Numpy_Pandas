import pandas as pd
import numpy as np

# Leggo i dati da un file csv
oil = pd.read_csv('retail/oil.csv').dropna()

# eseguo la iloc per selezionare le righe da 1000 a 1100
oil_array = np.array(oil['dcoilwtico'].iloc[1000:1100])

oil_series = pd.Series(oil_array, name='oil_prices')

dates = np.array(oil['date'].iloc[1000:1100])
oil_series.index = dates

print(oil_series)

def print_info(data_series):
    print(data_series.name)
    print(data_series.dtype)
    print(data_series.index)

def print_mean(data_series):
    mean = data_series.values.mean()
    print('La media è',mean)
    
    oil_series_int = data_series.astype('int')
    mean = oil_series_int.values.mean()
    print('La media dei numeri interi è',mean)
    
def print_mean_iloc(data_series, value):
    mean = data_series.iloc[:value].mean()
    print('La media dei primi 10 valori è',mean)
    
    mean = data_series.iloc[-value:].mean()
    print('La media degli ultimi 10 valori è',mean)

def print_lowest_prices(data_series, count):
    
    dates = [
        '2016-12-22',
        '2017-05-03',
        '2017-01-06',
        '2017-03-05',
        '2017-02-12',
        '2017-03-21',
        '2017-04-14',
        '2017-04-15',
    ]
    
    print(data_series.sort_values().iloc[:count].sort_index(ascending=False))
    print(data_series.loc[data_series.index.isin(dates)])
    #.loc[data_series.index.isin(dates)]

def print_less_price(data_series, price):
    print(data_series.loc[data_series < price])

def print_perc_difference(data_series):
    print('\nMAX VALUE\n')
    print(data_series.max())
    perc_series = (data_series - data_series.max()).abs().multiply(100).divide(data_series.max()).round(2)
    print(perc_series)

def print_quantile(data_series):
    x = data_series.quantile(0.1, interpolation='linear')
    print("10° quantile = "+str(x))
    y = data_series.quantile(0.9, interpolation='linear')
    print("90° quantile = "+str(y))

#print_mean_iloc(oil_series, 10)
print('\nLOWEST PRICE\n')
#print_lowest_prices(oil_series, 10)
print('\nLESS THAN PRICE\n')
#print_less_price(oil_series, 50)

#print(oil_series.multiply(1.1))
print_perc_difference(oil_series)

oil_series_counts = oil_series.astype('int').value_counts(normalize=True)
print(oil_series_counts)

print_quantile(oil_series)