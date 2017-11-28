from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import pandas as pd
import collections
import numpy as np
import warnings
warnings.filterwarnings('ignore')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

file = 'boliga_date_formatted.csv'
df = pd.read_csv(file)
columns_needed = df[['zip_code']]
columns_needed['zip_number'] = [int((el.split(' ')[0])) for el in df['zip_code'].values]
zip_counts = columns_needed['zip_number'].value_counts()
zips = columns_needed['zip_number'].unique()
zips.sort()

zip_sales = collections.OrderedDict()
x= []
y = []

for zip_no in zips:
    sales = len(columns_needed[columns_needed['zip_number'] == zip_no])
    zip_sales[zip_no] = sales


#get x and y values
x = []
y = []
for z, sales_number in zip_sales.items():
    x.append(z)
    y.append(sales_number)

hist, xedges, yedges = np.histogram2d(x, y, bins=(7, 7))
xpos, ypos = np.meshgrid(xedges[:-1] + xedges[1:], yedges[:-1] + yedges[1:])

xpos = xpos.flatten() /2
ypos = ypos.flatten() /2
zpos = np.zeros_like(xpos)

dx = xedges[1] - xedges[0]
dy = yedges[1] - yedges[0]
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='g', zsort='average')

plt.show()
