import os
import errno
import time
import random
import splinter
from selenium.webdriver.common.keys import Keys
from scraper import rand_wait_for_element
from scraper.config import NUMBEO_DIR
from scraper.util import utc_timestamp


class NumbeoScraper(object):
    """ Scrapes numbeo.com for cost of living data
    """
    def __init__(self, browser_type, force_reset=False):
        self.log_file = os.path.join(NUMBEO_DIR, 'log.txt')
        # Make sure output dirs are set up
        try:
            os.makedirs(NUMBEO_DIR)
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(NUMBEO_DIR):
                pass
            else:
                raise
        # Delete tracked log if force reset
        if force_reset:
            try:
                os.remove(self.log_file)
            except OSError:
                pass
        # Create new tracked log if it doesnt exist
        if not os.path.isfile(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write('# Numbeo scrape log\n# Started: {0}\n'.format(utc_timestamp()))
        self.browser_type = browser_type

    def scrape_cities(self, target_cities):
        """ Search for list of cities on numbeo and save output to dir
        """
        # Find which cities are already scraped from log
        with open(self.log_file, 'r') as f:
            log_lines = f.readlines()[2:]
        scraped_cities = [l.strip() for l in log_lines]
        new_cities = set(target_cities).difference(scraped_cities)
        new_cities.discard('')  # newline not a city
        total_new = len(new_cities)

        while len(new_cities) > 0:
            target_city = random.choice(tuple(new_cities))
            print('Scraping numbeo for {0} - {1}/{2}'.format(
                target_city, total_new - len(new_cities) + 1, total_new
            ))
            html = self.get_html_for_city(target_city)
            self.save_page(html, target_city)
            with open(self.log_file, 'a') as f:
                f.write('{0}\n'.format(target_city))
            new_cities.discard(target_city)

            time.sleep(random.randrange(4, 20))

        print('All cities scraped, complete!')


    def get_html_for_city(self, city):
        """ Launch browser, search for cities, and return html
        """
        with splinter.Browser(self.browser_type) as b:
            # visit home page
            b.visit('https://www.numbeo.com/cost-of-living/')
            # fill search form with city
            rand_wait_for_element(b, '//*[@id="dispatch_form"]')
            search_form = b.driver.find_element_by_xpath('//*[@id="city_selector_city_id"]')
            search_form.send_keys(city)
            time.sleep(5)
            search_form.send_keys(Keys.TAB)
            # close signup popup if exists
            try:
                b.find_by_xpath('/html/body/div[6]/div[1]/button').first.click()
            except splinter.exceptions.ElementDoesNotExist:
                pass
            # return search result
            return str(b.html)

    def save_page(self, html, city):
        filename = '{0}_{1}.html'.format(
           city.replace(',', '').replace(' ', '-'), utc_timestamp()
        )
        with open(os.path.join(NUMBEO_DIR, filename), 'w', encoding='utf-8') as f:
            f.write(html)

