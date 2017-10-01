import collections
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings('ignore')
import matplotlib

matplotlib.use('agg')
import matplotlib.pyplot as plt


def load_csv(csv_path, dtype=''):
    #dateparse = lambda x: pd.datetime.strptime(x, '%d-%m-%Y')

    if (dtype is ''):
        df = pd.read_csv(csv_path)
    else:
        df = pd.read_csv(csv_path, dtype=dtype, parse_dates=['sell_date'])#, date_parser=dateparse)

    return df


def data_handling(data):
    zip_df = pd.DataFrame(data['zip_code'].str.split(' ', 1).tolist(), columns=['zip', 'city'])
    data = data.assign(zip_int=zip_df['zip'])
    data['price_per_sq_m'] = pd.to_numeric(data['price_per_sq_m'], errors='coerce')
    data['zip_int'] = pd.to_numeric(data['zip_int'], errors='coerce')
    return data


def frequency_of_house_trades(data):
    unique_zips = data['zip_int'].unique()
    unique_zips.sort()
    # Sorted by order of insertion, so we sort the zips first.
    sales_by_zip = collections.OrderedDict()

    num_rooms_variance = range(1, 20)
    num_rooms_variance = [str(i) for i in num_rooms_variance]

    for zip in unique_zips:

        zip_df = data[data['zip_int'] == zip]
        rooms_dict = {}

        for room_amount in num_rooms_variance:
            occurences = len(zip_df[zip_df['no_rooms'] == room_amount])
            if occurences > 0:
                rooms_dict[room_amount] = occurences

        sales_by_zip[zip] = rooms_dict

    return sales_by_zip


def plot_on_histogram(data):
    fig = plt.figure()

    zip_ints = []
    rooms_dict = {}
    rooms_col = []
    highest_y = 0

    for zip, room_dict in data.items():
        rooms_amounts = []
        for rooms, amount in room_dict.items():
            if (amount > highest_y):
                highest_y = amount
            rooms_amounts.append(amount)
        rooms_col.append(rooms_amounts)
        zip_ints.append(zip)

    rooms_col = np.asarray(rooms_col)
    bins = len(rooms_col)

    n, bins, patches = plt.hist(rooms_col, bins, cumulative=True, histtype='bar', stacked=True, normed=1)

    fig.savefig('room_numbers_histogram.png')


def run():
    csv = load_csv('boliga_all_loc.csv', {'year_of_construction': str, 'no_rooms': str})
    reformatted_data = data_handling(csv)
    to_plot = frequency_of_house_trades(reformatted_data)
    plot_on_histogram(to_plot)


if __name__ == '__task5__':
    run()



