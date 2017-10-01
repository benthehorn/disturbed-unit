import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import math
import pandas as pd

norreport = (55.683669,12.571585)
file = 'boliga_date_formatted.csv'
df = pd.read_csv(file)
needed = df[['zip_code', 'sell_date', 'price_per_sq_m', 'lat', 'lon']]
needed['zip_number'] = [int((el.split(' ')[0])) for el in df['zip_code'].values]
needed['sell_year'] = [int(el.split('-')[-1]) for el in df['sell_date'].values]
data_set = needed[(needed['zip_number'] <= 3000) & (needed['sell_year'] == 15) & (needed['price_per_sq_m'] <= 80000)]
print(data_set.info())

def haversine_distance(origin, destination):

    lat_orig, lon_orig = origin
    lat_dest, lon_dest = destination
    radius = 6371

    dlat = math.radians(lat_dest-lat_orig)
    dlon = math.radians(lon_dest-lon_orig)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat_orig))
        * math.cos(math.radians(lat_dest)) * math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d

x = []
y = []

for d in data_set[['lat', 'lon', 'price_per_sq_m']].values:


    print(haversine_distance(norreport, (d[0],d[1])),d[2] )
    y.append(d[2])
    x.append(haversine_distance(norreport, (d[0],d[1])))


y.sort()
x.sort()

plt.plot(x,y)
plt.ylabel('Price per sqm')
plt.xlabel('Kms to Norreport')

plt.show()