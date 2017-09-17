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
