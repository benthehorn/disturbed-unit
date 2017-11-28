import warnings
warnings.filterwarnings('ignore')
from mpl_toolkits.basemap import Basemap
import pandas as pd
import matplotlib.pyplot as plt
import math

destination = (55.676111,12.568333)
x_coords_for_plot = []
y_coords_for_plot = []
file = 'boliga_date_formatted.csv'
df = pd.read_csv(file)
#take the last two digits to get the year
df['sell_year'] = [int(el.split('-')[-1])
                   for el in df['sell_date'].values]
#find entries from year 15
datedf = df[df['sell_year'] == 15]


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

for el in datedf[['lat', 'lon']].values:
#find any entries 50km or less from coords, and aa to array
    if haversine_distance(el, destination) <= 50:
        x_coords_for_plot.append(el[1])
        y_coords_for_plot.append(el[0])


#plot onto map
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None,
            width=10000000, height=10000000,
            lat_0=55, lon_0=10,)

x, y = m(x_coords_for_plot, y_coords_for_plot)
plt.plot(x, y, 'ok', markersize=5)
plt.show()