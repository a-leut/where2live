import json
from scraper.config import CITIES_FILE
from scraper.numbeo.numbeo_scraper import NumbeoScraper


def load_cities(file):
    """ Loads cities.json and returns list of cities
    """
    result = []
    with open(file, 'r') as f:
        d = json.loads(f.read())
        for row in d['result']:
            result.append('%s, %s' % (row['City'], row['State']))
    return result


def main():
    cities = load_cities(CITIES_FILE)
    scraper = NumbeoScraper('chrome')
    scraper.scrape_cities(cities)

if __name__ == '__main__':
    main()
