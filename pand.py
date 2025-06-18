import pandas as pd
import numpy as np
from scipy import stats
coffee = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
# print(coffee.sort_values(["Units Sold", "Coffee Type"], ascending=[False, True]))

# Filtering Data
bios = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv')
# print(bios[(bios['height_cm'] > 215) & (bios['born_country'] == 'USA')])
# print(bios[bios['name'].str.contains('raha', case=False)])
# bios.query('born_country == "USA" and born_city == "Seattle"')

# Adding/Removing Columns
coffee['price'] = 4.99
coffee['new_price'] = np.where(coffee['Coffee Type']=='Espresso', 3.99, 5.99)
coffee.drop(columns=['price'], inplace=True)
# or coffee = coffee.drop(columns=['price'])
coffee['revenue'] = coffee['Units Sold'] * coffee['new_price']
coffee.rename(columns={'new_price': 'price'})

# To get only the first name in bios
# bios_new = bios.copy()
# bios_new['first_name'] = bios_new['name'].str.split(' ').str[0]
# bios_new.drop(columns=['name'], inplace=True)
# bios_new['born_datetime'] = pd.to_datetime(bios_new['born_date'])
# bios_new.drop(columns=['born_date'], inplace=True)
# bios_new['born_year'] = bios_new['born_datetime'].dt.year
# To save in the csv file from here :- bios_new.to_csv('bios.csv', index=False)
# bios['height_category'] = bios['height_cm'].apply(lambda x: "Short" if x < 165 else ("Average" if x < 185 else 'Tall'))


def categorize_athletes(row):
    if row['height_cm'] < 175 and row['weight_kg'] < 70:
        return 'Light Weight'
    elif row['height_cm'] < 185 or row['weight_kg'] <= 80:
        return 'MiddleWeight'
    else:
        return 'Heavy Weight'


# bios['Category'] = bios.apply(categorize_athletes, axis=1)

# Merging and Concatenating Data
nocs = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/noc_regions.csv')
bios_new = pd.merge(bios, nocs, left_on='born_country', right_on='NOC', how='left')
bios_new.rename(columns={'region': 'born_country_full'}, inplace=True)
# usa = bios[bios['born_country']=='USA'].copy()
# gbr = bios[bios['born_country']=='GBR'].copy()
# new_df = pd.concat([usa, gbr])
# results = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/results.csv')
# combined_df = pd.merge(results, bios, on='athlete_id', how='left')
# print(combined_df.head())

# Handling Null values

coffee.loc[[0, 1], 'Units Sold'] = np.nan
# coffee = coffee.fillna(coffee['Units Sold'].mean())
# we can also do coffee = coffee.fillna(coffee['Units Sold'].interpolate())
# we can also do coffee.dropna(subset=['Units Sold'], inplace=True), this drops all the rows having the specified columns as NaN
# print(coffee[coffee['Units Sold'].isna()])

# Aggregating data
# print(bios[bios['born_country'] == 'IND']['born_region'].value_counts())
# print(coffee.groupby(['Coffee Type']).agg({'Units Sold': 'sum', 'new_price': 'mean'}))
pivot = coffee.pivot(columns='Coffee Type', index='Day', values='revenue')
# print(pivot.sum(axis=1))
# bios['born_date'] = pd.to_datetime(bios['born_date'])
# print(bios.groupby(bios['born_date'].dt.year)['name'].count().reset_index().sort_values('name', ascending=False))

# advanced functionalities :- .shift(), .rank(), .rolling(), .cumsum()
coffee["yesterday_revenue"] = coffee['revenue'].shift(2)
coffee['pct_change'] = coffee['revenue'] / coffee['yesterday_revenue']
bios['height_rank'] = bios['height_cm'].rank()
# print(bios.sort_values(['height_rank'], ascending=False))
coffee['cumulative_revenue'] = coffee['revenue'].cumsum()
latte = coffee[coffee['Coffee Type'] == 'Latte'].copy()
latte['3day'] = latte['Units Sold'].rolling(3).sum()
print(latte)