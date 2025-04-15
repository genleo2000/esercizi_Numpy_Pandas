import pandas as pd

insurance_df = pd.read_csv('assignment/retail/insurance_data.csv')

# Create a MultiIndex DataFrame by grouping and calculating mean charges
multi_index_df = insurance_df.groupby(['region','smoker'])[['charges']].mean()
print(type(multi_index_df))
print(multi_index_df)

print(multi_index_df.reset_index())