import pandas as pd

df = pd.read_csv('assignment/retail/oil.csv')
data_2014 = df.loc[df['date'].str[:4] == '2015']

print(data_2014.head(20))

data_sql = df.query('dcoilwtico > 90')
print(data_sql.head(20))

price_mean = df['dcoilwtico'].mean()
print(price_mean)

data_sql = df.query('dcoilwtico > @price_mean').sort_values('dcoilwtico')
print(data_sql.head(20))

stores = pd.read_csv('assignment/retail/stores.csv')
res = stores.query('city == "Quito"')
print(res.head(20))