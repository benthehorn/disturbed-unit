import os
import bs4
import re
import requests
import csv
import pprint

pp = pprint.PrettyPrinter(indent=4)
BASE_URL = 'http://138.197.184.35/boliga/'

out_dir = './data/out'
if not os.path.exists(out_dir):
    os.mkdir(out_dir)


def connect_and_retrieve_boliga_atags(url):
    # Sending a request to the specified URL:
    r = requests.get(url)

    # Make sure we get notified in case of a bad request:
    if r is None:
        r.raise_for_status()

    # Save the content from the Response Object:
    soup = bs4.BeautifulSoup(r.text, 'html5lib')

    # Isolating all the a-tags to scrape:
    a_tags = soup.find_all('a')

    return a_tags


# Returning the hrefs alone, filtered (must start with a number if it's a zip code):
def filter_hrefs(tags):
    hrefs = []
    for a in tags:
        url = a.get('href')
        match_obj = re.match('.*([.,/])html$', url)
        if match_obj:
            hrefs.append(url)
        else:
            continue
    return hrefs


def scrape_housing_data(url):
    data = []
    s = requests.get(url)
    sup = bs4.BeautifulSoup(s.content.decode('utf-8'), 'html5lib')
    table = sup.find('table')
    tBody = table.find('tbody')

    rows = tBody.find_all('tr')
    for row in rows:
        cols = row.find_all('td')

        # Decode address column
        address_str = cols[0].text.strip()
        zip_number = str(get_num(address_str))[-4:]

        # Decode price
        price = cols[1].text.strip()
        split_price = price.split('.')
        join_price = ''.join(split_price)
        price = int(join_price)

        # Decode sales date and type
        string = cols[2].text.strip()
        array = re.split(r'([A-Za-z\s.]+)', string)
        sell_date = array[0]
        sell_type = array[1]

        # Decode price per squere meter
        size_in_sq_m_str = cols[3].text.strip()
        sq_price_split = size_in_sq_m_str.split('.')
        price_per_sq_m = ''.join(sq_price_split)

        # Decode number of rooms
        no_rooms_str = cols[4].text.strip()
        no_rooms = no_rooms_str

        # Decode type of housing
        housing_type = cols[5].text.strip()

        # Decode room size
        room_size = cols[6].text.strip()
        size_in_sq_m = room_size


        # Decode year of construction
        year_of_construction_str = cols[7].text.strip()
        year_of_construction = year_of_construction_str

        # Decode price change
        price_change_in_pct = cols[8].text.strip()
        # price_change_in_pct = int(price_change_in_pct_str)

        decoded_row = (address_str, zip_number, price, sell_date, sell_type, price_per_sq_m,
                       no_rooms, housing_type, size_in_sq_m, year_of_construction, price_change_in_pct)
        data.append(decoded_row)
        # pp.pprint(data)

    return data


def save_to_csv(data, path='/boliga.csv'):
    with open(path, 'w', encoding='utf-8') as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(['address_str', 'zip_number', 'price',
                                'sell_date', 'sell_type',
                                'price_per_sq_m', 'no_rooms',
                                'housing_type', 'size_in_sq_m', 'year_of_construction', 'price_change_in_pct'])

        for row in data:
            output_writer.writerow(row)


def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))


def run():
    tags = connect_and_retrieve_boliga_atags(BASE_URL)
    urls_endings = filter_hrefs(tags)
    for url in urls_endings:
        housing_data = scrape_housing_data(BASE_URL + url)
        save_to_file = os.path.join(out_dir, url.split('_')[1] + '.csv')
        save_to_csv(housing_data, save_to_file)


if __name__ == '__main__':
    run()
