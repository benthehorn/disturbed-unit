# Assignment 3 for Business Intelligence
#### By Disturbed Unit
# Getting Started.
All files refered to are in the assignment-3 directory.

The osm file with all the address data in is huge, so we used osmconvert64 to trim some of the un_needed data.
This method was posted by one of the other members of class who was also finding that the process was stopping, due to memory leakage.
We install add the binaries to our Git/mingw64/bin directory, and run the following from the directory of the .osm file:

 osmconvert64 denmark-latest-osm --drop-ways --drop-relations > trimmed-denmark_latest.osm

This command writes a new file, but removes the <way> and <relation> elements, and the file is now approximately 1GB smaller.
We next used the XMLBreaker script from https://gist.github.com/nicwolff/b4da6ec84ba9c23c8e59 that slpits the file into more manageable chunks. After this we had no more crashes, and the data converted to csv format without incident!
 
 1. Read the entire dataset of Danish housing sales data, see Assignment 2, into a Pandas `DataFrame`. Use the `read_csv` function from the `pandas` module.


  * Geocode the the entire dataset of Danish housing sales data, see Assignment 2. Add two new columns to the `DataFrame`, one for latitude (`lat`) and one for longitude (`lon`) coordinates per address. Do the geocoding with help of the OSM dataset stored in a file as discussed in class. Save that `DataFrame` to a CSV file with the help of pandas
  
The code we used to then add the GeoData to the csv file we got can be found in the file addGeoCode.py. This part of the process follows the examples from the lecture_notes, with a few modifications.

If our data from the scraping exercise was formatted correctly, this code would take every node from the csv file created earlier, and extract the address:street, housenumber,postcode and city, and add these to a new csv file. At the same time, it should run the geolocate_dataframe method, and find any matches by these properties, and add the lat and lon geotags to the sales information. This doesn't happen. Our data is improperly formatted and so the method doesn't find the matches, leaving us with empty lat and lon columns.

At the time of writing, we are scraping the data again, but time has run out, again.
  


 * Convert all sales dates in the dataset into proper `datetime` objects.
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


* Compute the average price per square meter for the years 1992 and 2016 respectively for the city centers of Copenhagen (zip code 1050-1049), Odense (zip code 5000), Aarhus (zip code 8000), and Aalborg (zip code 9000). Create two new `DataFrame`s, one for the year 1992 and one for the year 2016, which contain the respective zip codes and the average price per square meter corresponding to the aforementioned cities. Let the `DataFrame`s be sorted by ascending prices.

Using some of the example code from the lecture notes I started to experimient with trying to get the data needed to calulate the average prices per sq. metre. Again, the fact that we have not formatted the data properly makes this impossible.

But the averageprice.py file takes the csv as a dataframe, and then splits it into new frames based on post code. Then we can further reduce the dataframe by year, at which point we would get all the prices, convert them from string to float, and calulate the average prices for each dataframe. Once we get our data in order we should be able to complete this step.

* Create, with the help of the `pandas` module, four new CSV files containing the sales data for the year 1992 for the city centers of Copenhagen (zip code 1050-1049), Odense (zip code 5000), Aarhus (zip code 8000), and Aalborg (zip code 9000).
```
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
```
 * Use the following function, which computes the Haversine Distance (https://en.wikipedia.org/wiki/Haversine_formula) to compute an array of distances (`distances`) for each for each location in the dataset of Danish housing sales data to the city center of Roskilde (lat=55.65, lon=12.083333).

  ```python
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
  ```
  In the haversine.py file I have made an example of this using the coordinates in the lecture notes, so that we can see how it works.
  We will make the graph work..
