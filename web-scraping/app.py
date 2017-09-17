import bs4
import re
import requests


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
def sort_hrefs(tags):
    hrefs = []
    for a in tags:
        url = a.get('href')
        match_obj = re.match('.*([.,/])html$', url)
        if match_obj:
            hrefs.append(url)
        else:
            continue
    return hrefs


def run():
    tags = connect_and_retrieve_boliga_atags('http://138.197.184.35/boliga/')
    urls = sort_hrefs(tags)
    print(urls[:20])


if __name__ == '__main__':
    run()

    
    
    
    import bs4
import requests
import csv
import re

base_url = 'http://138.197.184.35/boliga/'
r = requests.get(base_url)
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html5lib')

a_elems = soup.select('a')

# Returning the hrefs alone, filtered (must start with a number if it's a zip code):
def sort_hrefs(tags):
    hrefs = []
    for a in tags:
        url = a.get('href')
        match_obj = re.match('.*([.,/])html$', url)
        if match_obj:
            hrefs.append(url)
        else:
            continue
    return hrefs

a_filtered = sort_hrefs(a_elems)
    
print(len(a_elems))
print(len(a_filtered))

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
        #street_str = ' '.join(address_str.split(' ')[:-3])
        #city_str = ' '.join(address_str.split(' ')[-3:])
        #zip_number = int(address_str.split(' ')[-3])

        # Decode price
        price = cols[1].text.strip()
        #price = float(price_str)
        
        # Decode sales date and type
        string = cols[2].text.strip()
        sell_date = ' '.join(string.split(' ')[:-1])
        sell_type = ' '.join(string.split(' ')[-1:])
        
        # Decode price per squere meter
        size_in_sq_m_str = cols[3].text.strip()
        price_per_sq_m = float(size_in_sq_m_str)
        
        # Decode number of rooms
        no_rooms_str = cols[4].text.strip()
        no_rooms = int(no_rooms_str)
        
        # Decode type of housing
        housing_type = cols[5].text.strip()
        
        # Decode room size
        room_size = cols[6].text.strip()
        size_in_sq_m = int(room_size)
        
        # Decode year of construction
        year_of_construction_str = cols[7].text.strip()
        year_of_construction = int(year_of_construction_str)
        
        # Decode price change
        price_change_in_pct = cols[8].text.strip()
        #price_change_in_pct = int(price_change_in_pct_str)
        
        decoded_row = (address_str, price, sell_date, sell_type, price_per_sq_m,
                      no_rooms, housing_type, size_in_sq_m, year_of_construction, price_change_in_pct)
        data.append(decoded_row)
        
    print('Scraped {} sales...'.format(len(data)))
    
    return data

base_url = 'http://138.197.184.35/boliga/1050-1549_1.html' 
housing_data = scrape_housing_data(base_url)
housing_data[:3]
