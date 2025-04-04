import pandas as pd

df = pd.read_csv('assignment/retail/retail_2016_2017.csv')

df = df.astype({'family':'category'})

print(df.head(20))

# il parametro memory_usage='deep' permette di calcolare la memoria occupata da ogni colonna, in modo approfondito
# comprese quelle di tipo object e category
df.info(memory_usage='deep')


print(df.memory_usage(deep=True))

# andiamo ad ottimizzare il tipo di dato della colonna date, che è di tipo object
df = df.astype({'date':'datetime64[ns]'})

print(df.memory_usage(deep=True))