import pandas as pd

#read csv file and parse column 3 to date format
df = pd.read_csv('boliga_all.csv')

df['sell_date'] = pd.to_datetime(df['sell_date'])
new_file = df[df['sell_date']]
# save new file with parsed date
new_file.to_csv("newFile.csv", index=False)

#check if data been parsed
f = pd.read_csv("newFile.csv")
f.head()
