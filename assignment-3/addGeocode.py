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

    focusFrame = sale_data_frame
    focusFrame['lat'] = np.nan
    focusFrame['lon'] = np.nan

    df.setupDataFrameCsv()

    dataFrame = ConcatAddandZip(focusFrame)

    dataFrame.set_index("api_addresses", inplace=True)

    pbar = tqdm()

    for file in os.listdir('/data/osm/'):
        if not file.endswith('xml'): continue
        for idx, decoded_node in enumerate(decode_node_to_csv(file)):
            try:
                full_address = decoded_node.tags['addr:street'].encode('utf8') + " " + decoded_node.tags['addr:housenumber'].encode('utf8') + " " + \
                               decoded_node.tags['addr:postcode'].encode('utf8') + " " + decoded_node.tags['addr:city'].encode('utf8')
                addr_with_geo = (full_address, decoded_node.lon, decoded_node.lat)

                write_to_csv(addr_with_geo, "data/addresses1.csv")

                pbar.update()

                geolocate_dataframe(focusFrame, addr_with_geo)

            except (KeyError, ValueError):
                pass
        print('Finished with: ' + file)

    df.write_df_ToCsv(focusFrame, "data/sales_with_geocode.csv")



def ConcatAddandZip(dFrame):
    api_addresses = [' '.join([a.split(',')[0], z]) for a, z in dFrame[[('address').replace("\"", ""), 'zip_code']].values]
    dFrame = dFrame.assign(api_addresses=api_addresses)
    dFrame = dFrame.drop_duplicates(subset="api_addresses")

    return dFrame


def geolocate_dataframe(dataframe, addr_with_geo):

    if dataframe.loc[addr_with_geo[0]] is not None:
        dataframe.set_value(addr_with_geo[0],'lon',addr_with_geo[1])
        dataframe.set_value(addr_with_geo[0],'lat',addr_with_geo[2])


def write_to_csv(string, output_path):
    # print(string)

    with open(output_path, 'a') as f:
        output_writer = csv.writer(f)
        output_writer.writerow(string)

