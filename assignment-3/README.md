# Assignment 3 for Business Intelligence
#### By Disturbed Unit
# Getting Started.
The osm file with all the address data in is huge, so we used osmconvert64 to trim some of the un_needed data.
This method was posted by one of the other members of class who was also finding that the process was stopping, due to memory leakage.
We install add the binaries to our Git/mingw64/bin directory, and run the following from the directory of the .osm file:

 osmconvert64 denmark-latest-osm --drop-ways --drop-relations > trimmed-denmark_latest.osm

This command writes a new file, but removes the <way> and <relation> elements, and the file is now approximately 1GB smaller.
We next used the XMLBreaker script from https://gist.github.com/nicwolff/b4da6ec84ba9c23c8e59 that slpits the file into more manageable chunks. After this we had no more crashes, and the data converted to csv format without incident!
  
The code we used to then add the GeoData to the csv file we got can be found in the file addGeoCode.py. This part of the process follows the examples from the lecture_notes, with a few modifications.

If our data from the scraping exercise was formatted correctly, this code would take every node from the csv file created earlier, and extract the address:street, housenumber,postcode and city, and add these to a new csv file. At the same time, it should run the geolocate_dataframe method, and find any matches by these properties, and add the lat and lon geotags to the sales information. This doesn't happen. Our data is improperly formatted and so the method doesn't find the matches, leaving us with empty lat and lon columns.

At the time of writing, we are scraping the data again, but time has run out, again.
  


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
