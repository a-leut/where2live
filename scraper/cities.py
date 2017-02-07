import requests
import pandas as pd
from lxml import html

def get_cities():
    # download list of most populous cities from wikipedia
    r = requests.get('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population')
    pd.read_html(r.text, )
    #tree = html.parse(r.text)
    #table = tree.xpath('//*[@id="mw-content-text"]/table[4]')[0]
    #raw_html = html.tostring(table)

    #print(raw_html)

get_cities()
