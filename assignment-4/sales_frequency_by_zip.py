import pandas as pd
import matplotlib.pyplot as plt


file = 'boliga_date_formatted.csv'
df = pd.read_csv(file)
columns_needed = df[['zip_code']]

columns_needed['zip_number'] = [int((el.split(' ')[0])) for el in df['zip_code'].values]
zip_counts = columns_needed['zip_number'].value_counts()
sorted_by_zip = zip_counts.sort_index()


x = []
y = []
for zip, sales_number in sorted_by_zip.iteritems():
    print(zip, sales_number)
    x.append(zip)
    y.append(sales_number)
plt.figure(figsize=(60,15))
plt.plot(x, y)
#when using plot.bar we we don't get all of the information displayed. the plot gives a better view..
plt.show()