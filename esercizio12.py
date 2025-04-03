import pandas as pd

df = pd.read_csv('assignment/retail/oil.csv')
print(df.head(20))

df.dropna(subset=['dcoilwtico'], inplace=True)
print(df.head(20))

df['distanza'] = (df['dcoilwtico'] - df['dcoilwtico'].mean()) ** 2

print(df.head(20))

print(df['distanza'].sum() / (df['distanza'].count() - 1))
print(df['dcoilwtico'].var())

df['superiore_media'] = df['dcoilwtico'] > df['dcoilwtico'].mean()
print(df.head(20))

print((df.loc[df['superiore_media'] == False]).head(20))