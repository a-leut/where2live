import os

PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
CITIES_FILE = os.path.join(PARENT_DIR, 'scraper', 'clean_cities.csv')
NUMBEO_DIR = os.path.join(PARENT_DIR, 'data', 'numbeo')