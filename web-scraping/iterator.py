import bs4
import csv
import re
import urllib
from urllib.request import urlopen

Url = 'http://138.197.184.35/boliga'
FullUrl = 'http://138.197.184.35/boliga/1050-1549_1.html'
Page = urlopen(Url)
Page1 = urlopen(FullUrl)


def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))
# we can use this to write each csv file, by changing some of the parameters..I think
def save_to_csv(data, path='./out/boliga.csv'):
    with open(path, 'w', encoding='utf-8') as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(['address', 'zip_code', 'price', 'sell_date', 'sell_type',
                                'price_per_sq_m', 'no_rooms', 'housing_type', 'size_in_sq_m',
                                'year_of_construction', 'price_change_in_pct'])

        for row in data:
            output_writer.writerow(row)


URLendings = []
soup = bs4.BeautifulSoup(Page, "html5lib")
table = soup.find_all("a")

Complete = []
for t in table:
    URLendings.append(t.get('href'))
    num = len(URLendings)
    #print(t.get('href'))
    #print(num)

    for url in URLendings[5:]:
        full = Url + '/' + url
        fullUrl1 = urlopen(full)
        soup1 = bs4.BeautifulSoup(fullUrl1, "html5lib")

        # Info = [];
        # soup1 = bs4.BeautifulSoup(Page1, "html5lib")
        table1 = soup1.find("table")
        body = table1.find('tbody')
        rows = body.find_all('tr')
        for row in rows:

            cols = row.find_all('td')
            # Decode address column
            address_str = cols[0].text.strip()
            zip_number = str(get_num(address_str))[-4:]
            address = address_str.split(zip_number)
            fulladdress = address[0] + ' ' + address[1]
            #print(fulladdress)
            #print(zip_number)


            Complete.append([fulladdress, zip_number])
            print(len(Complete))



