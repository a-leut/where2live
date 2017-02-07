import json
from scraper.config import CITIES_FILE
from scraper.numbeo.numbeo_scraper import NumbeoScraper

def main():
    # load cities
    with open(CITIES_FILE, 'r') as f:
        cities = f.read().split('\n')[1:]
    scraper = NumbeoScraper('phantomjs')
    scraper.scrape_cities(cities)

if __name__ == '__main__':
    main()
