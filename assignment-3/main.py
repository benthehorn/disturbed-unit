import dataFrameMaker as df
import addGeocode as ag
import dateformatter as date
#import averageprice as av



def run():

    frame = df.read_csv("all_sales.csv")
    date.format_dates(frame)
    new_frame = df.read_csv("date_formatted_sales.csv")
    ag.addGeocode(new_frame)
    #av.find_averages(new_frame)
    #doesn't work yet.
run()