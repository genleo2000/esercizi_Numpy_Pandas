import pandas as pd

df = pd.read_csv('retail/insurance_data.csv')
print(df.head(20))

# Create a new column 'tax_amount' based on conditions
# Assume a tax rate of 5% on the charges for smokers over 18 years old
df['tax_amount'] = 0
df.loc[(df['smoker'] == 'yes') & (df['age'] > 18), 'tax_amount'] = df['charges'] * 0.05

print(df.head(20))

print(type(df.loc[:, 'region']))
print(type(df['region']))