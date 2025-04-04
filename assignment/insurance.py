import pandas as pd
import numpy as np

df = pd.read_csv('retail/insurance_data.csv')
print(df.head(20))

# Create a new column 'tax_amount' based on conditions
# Assume a tax rate of 5% on the charges for smokers over 18 years old
df['tax_amount'] = 0
df.loc[(df['smoker'] == 'yes') & (df['age'] > 18), 'tax_amount'] = df['charges'] * 0.05

print(df.head(20))

#print(type(df.loc[:, 'region']))
#print(type(df['region']))

conditions = [(df['sex'] == 'male') & (df['age'] > 30), 
                (df['sex'] == 'female') & (df['children'] > 0)
            ]

choises = [(df['charges'] * 0.05),(df['charges'] * 0.05)]
label = ['Età avanzata','Madre con figli']

# Si possono dare in pasto alla funzione assign()
df['ohter_tax'] = np.select(conditions, choises, default=0)
df['category'] = np.select(conditions, label, default='')

print(df.head(20))
print(df['category'].value_counts())

mapping = {'southwest': 'SW','northeast': 'NE','southeast': 'SE','northwest': 'NW'}

# df['region'] è una serie, quindi possiamo usare il metodo map( con un dizionario per mappare i valori
df['region'] = df['region'].map(mapping)

# la funzione map() lavora su una serie e restituisce una serie
df = df.assign(genitore=(df['children'] > 0).map({True: 'Genitore', False: 'Non genitore'}))

# df['sex'].str[0] , la funzione str[] permette di accedere a una stringa come se fosse una lista
df = df.assign( sex_abbrev = df['sex'].str[0], high_risk = lambda x: (x['sex_abbrev'] == 'm') & (x['bmi'] > 27.5) )

print(df[['sex','sex_abbrev','high_risk']])
