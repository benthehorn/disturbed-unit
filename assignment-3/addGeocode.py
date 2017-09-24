import pandas as panda
import numpy as np
import os
import csv
import io_handler as io
from tqdm import tqdm
from osmread import parse_file, Node
import dataFrameMaker as df

def decode_node_to_csv(filename):
    for entry in parse_file('/data/osm/' + filename):

        if (isinstance(entry, Node) and
                    'addr:street' in entry.tags and
                    'addr:postcode' in entry.tags and
                    'addr:housenumber' in entry.tags and
                    'addr:city' in entry.tags):
            yield entry

def addGeocode(sale_data_frame):
    progress_bar = tqdm()
    focus_frame = sale_data_frame
    focus_frame['lat'] = np.nan
    focus_frame['lon'] = np.nan

    df.setupDataFrameCsv()

    data_frame = concat_and_zip(focus_frame)

    data_frame.set_index("api_addresses", inplace=True)



    for file in os.listdir('/data/osm/'):
        if not file.endswith('xml'): continue
        for idx, decoded_node in enumerate(decode_node_to_csv(file)):
            try:
                full_address = decoded_node.tags['addr:street'].encode('utf8') + " " + decoded_node.tags['addr:housenumber'].encode('utf8') + " " + \
                               decoded_node.tags['addr:postcode'].encode('utf8') + " " + decoded_node.tags['addr:city'].encode('utf8')
                addr_with_geo = (full_address, decoded_node.lon, decoded_node.lat)

                write_to_csv(addr_with_geo, "data/addresses1.csv")

                progress_bar.update()

                geolocate_dataframe(focus_frame, addr_with_geo)

            except (KeyError, ValueError):
                pass
        print('Done: ' + file)

    df.write_df_ToCsv(focus_frame, "data/sales_with_geocode.csv")



def concat_and_zip(d_frame):
    api_addresses = [' '.join([a.split(',')[0], z]) for a, z in dFrame[[('address').replace("\"", ""), 'zip_code']].values]
    d_frame = d_frame.assign(api_addresses=api_addresses)
    d_frame = d_frame.drop_duplicates(subset="api_addresses")

    return d_frame


def geolocate_dataframe(data_frame, geo_add):

    if data_frame.loc[geo_add[0]] is not None:
        data_frame.set_value(geo_add[0],'lon',geo_add[1])
        data_frame.set_value(geo_add[0],'lat',geo_add[2])


def write_to_csv(string, output_path):
    # print(string)

    with open(output_path, 'a') as f:
        output_writer = csv.writer(f)
        output_writer.writerow(string)

