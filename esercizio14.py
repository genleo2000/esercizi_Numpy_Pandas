import pandas as pd

insurance_df = pd.read_csv('assignment/retail/insurance_data.csv')

# TEST 1

# Create a MultiIndex DataFrame by grouping and calculating mean charges
#multi_index_df = insurance_df.groupby(['region','smoker'])[['charges']].mean()
#print(type(multi_index_df))
#print(multi_index_df)

#print(multi_index_df.reset_index())

# TEST 2

#aggregated_data = insurance_df.groupby(['region','smoker']).agg(carges_sum=('charges','sum'),charges_mean=('charges','mean'),children_max=('children','max'))
#print(aggregated_data)

# TEST 3
pivot_table = insurance_df.query("smoker == 'yes' and region in ['southeast','northwest']").pivot_table(index='region',values='charges',aggfunc='sum')

# Display the pivot table
print(pivot_table)
