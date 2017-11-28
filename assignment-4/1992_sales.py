import folium
import pandas as pd

my_map = folium.Map(location=[55.88207495748612, 10.636574309440173], zoom_start=6)

# fetch all city sales onf 1992
df_Aarhus = pd.read_csv('Aarhus_1992.csv')
df_odense = pd.read_csv('Odense_1992.csv')
df_alborg = pd.read_csv('alborg_1992.csv')
df_Kobenhavn = pd.read_csv('København_K_1992.csv')

# merge all data frames into one data frame
frames = [df_alborg, df_Aarhus, df_odense, df_Kobenhavn]
result = pd.concat(frames)

# create a mask
mask = ((~result.lat.isnull()) &
       (~result.lon.isnull()))

df_1992 = result[mask]

for coords in zip(df_1992.lon.values, 
                  df_1992.lat.values):
    folium.CircleMarker(location=[coords[1], coords[0]], radius=2).add_to(my_map)

# save into file
#my_map.save('1992_sales.html')

# display result
my_map
