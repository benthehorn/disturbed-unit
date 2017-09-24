import pandas as pd
import re

#read csv file
df = pd.read_csv('newFile.csv')

# parse sell_date to date time format
df['sell_date'] = pd.to_datetime(df['sell_date'])

#fetch data by criteria
Aarhus_1992 = df[(df['zip_code'] == '8000 Aarhus C') & (df['sell_date'].dt.year == 1992)]
alborg_1992 = df[(df['zip_code'] == '9000 Aalborg') & (df['sell_date'].dt.year == 1992)]
Odense_1992 = df[(df['zip_code'] == '5000 Odense C') & (df['sell_date'].dt.year == 1992)] 
København_K_1992 = df['zip_code'].str.contains('København K') & (df['sell_date'].dt.year == 1992) 

# save new files with filtered data
Aarhus_1992.to_csv("Aarhus_1992.csv", index=False)
alborg_1992.to_csv("alborg_1992.csv", index=False)
Odense_1992.to_csv("Odense_1992.csv", index=False)
København_K_1992.to_csv("København_K_1992.csv", index=False)

print('done')
