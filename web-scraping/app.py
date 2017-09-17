import os
import csv
import bs4
import re
import requests

# Sending a request to the specified URL:
r = requests.get('http://138.197.184.35/boliga/')

# Make sure we get notified in case of a bad request:
if r is None:
    r.raise_for_status()

# Save the content from the Response Object:
soup = bs4.BeautifulSoup(r.text, 'html5lib')

# Isolating all the a-tags to scrape:
a_tags = soup.find_all('a')

# Returning the hrefs alone, sorted (must start with a number if it's a zip code):
hrefs = []
for a in a_tags:
    url = a.get('href')
    matchObj = re.match('.*([.,/])html$', url)
    if matchObj:
        hrefs.append(url)
    else:
        continue

    def save_to_csv(data, path='./out/boliga.csv'):
        with open(path, 'w', encoding='utf-8') as output_file:
            output_writer = csv.writer(output_file)
            output_writer.writerow(['street', 'city', 'zipcode',
                                    'no_rooms', 'size_in_sq_m',
                                    'year_of_construction', 'price',
                                    'sale_date_str'])

            for row in data:
                output_writer.writerow(row)


    out_dir = './data/out'
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

#
# # print(soup.prettify())
# print(type(elems))
# print(len(elems))
# print(type(elems[0]))
# print(elems[0].getText())
# print(elems[0].text)
# print(str(elems[0]))
# print(elems[0].attrs)
# print(elems[0].contents)
#
# p_elems = soup.select('p')
#
# for el in p_elems:
#     # str(p_elems[0]), str(p_elems[1]),...
#     print(str(el))
#     print(el.getText())
#     print('------------')
#
# span_elem = soup.select('span')[0]
# print(str(span_elem))
# print(span_elem.get('id'))
# print(span_elem.get('some_nonexistent_addr') == None)
# print(span_elem.attrs)
#
#
# def scrape_housing_data(url):
#     data = []
#
#     r = requests.get(url)
#     soup = bs4.BeautifulSoup(r.content.decode('utf-8'), 'html5lib')
#
#     table = soup.find('table')
#     table_body = table.find('tbody')
#
#     rows = table_body.find_all('tr')
#     for row in rows:
#         cols = row.find_all('td')
#
#         # Decode address column
#         address_str = cols[0].text.strip()
#         street_str = ' '.join(address_str.split(' ')[:-3])
#         city_str = ' '.join(address_str.split(' ')[-3:])
#         zip_number = int(address_str.split(' ')[-3])
#
#         # Decode number of rooms
#         no_rooms_str = cols[1].text.strip()
#         no_rooms = int(no_rooms_str)
#
#         # Decode selling date and type
#         size_in_sq_m_str = cols[2].text.strip()
#         size_in_sq_m = int(size_in_sq_m_str)
#
#         # Decode year of construction
#         year_of_construction_str = cols[3].text.strip()
#         year_of_construction = int(year_of_construction_str)
#
#         # Decode price
#         price_str = cols[4].text.strip()
#         price = float(price_str)
#
#         # Decode sales date
#         sale_date_str = cols[5].text.strip()
#
#         decoded_row = (street_str, city_str, zip_number, no_rooms,
#                        size_in_sq_m, year_of_construction, price,
#                        sale_date_str)
#         data.append(decoded_row)
#
#     print('Scraped {} sales...'.format(len(data)))
#
#     return data
#
#
# base_url = 'http://127.0.0.1:8888/files/data/boliga_1050-1549_1.html'
# housing_data = scrape_housing_data(base_url)
# housing_data[:3]
#
#

#
# base_url = 'http://127.0.0.1:8888/files/data'
# urls = ['boliga_1050-1549_1.html', 'boliga_1050-1549_2.html', 'boliga_1550-1799_1.html']
# urls = [os.path.join(base_url, url) for url in urls]
#
# fst_fourty_results = scrape_housing_data(urls[0])
# snd_fourty_results = scrape_housing_data(urls[1])
# fst_results = fst_fourty_results + snd_fourty_results
#
# save_to_file = os.path.join(out_dir, os.path.basename(urls[0]).split('_')[1] + '.csv')
# save_to_csv(fst_results, save_to_file)
#
# last_results = scrape_housing_data(urls[2])
# save_to_file = os.path.join(out_dir, os.path.basename(urls[2]).split('_')[1] + '.csv')
# save_to_csv(last_results, save_to_file)
