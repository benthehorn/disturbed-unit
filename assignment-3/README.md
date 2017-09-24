# Assignment 1 for Business Intelligence
#### By Disturbed Unit

2. Convert all sales dates in the dataset into proper `datetime` objects.
```
import pandas as pd

#read csv file and parse column 3 to date format
df = pd.read_csv('boliga_all_3.csv', parse_dates = [3])

print('done')

# save new file with parsed date
df.to_csv("newFile.csv", index=False)

#check if data been parsed
f = pd.read_csv("newFile.csv")
f.head()
```
