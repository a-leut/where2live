import os
import datetime
import errno
import time
import splinter
from selenium.webdriver.common.keys import Keys
from scraper import rand_wait_for_element
from scraper.config import NUMBEO_DIR

class NumbeoScraper(object):
    """ Scrapes numbeo.com for cost of living data
    """
    def __init__(self, browser):
        self.browser = browser
        # make sure output dirs are set up
        try:
            os.makedirs(NUMBEO_DIR)
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(NUMBEO_DIR):
                pass
            else:
                raise

    def scrape_cities(self, cities):
        for city in cities:
            html = self.get_html_for_city(city)
            self.save_page(html, city)

    def get_html_for_city(self, city):
        with splinter.Browser(self.browser) as b:
            # visit home page
            b.visit('https://www.numbeo.com/cost-of-living/')
            # fill search form with city
            rand_wait_for_element(b, '//*[@id="dispatch_form"]')
            search_form = b.driver.find_element_by_xpath('//*[@id="city_selector_city_id"]')
            search_form.send_keys(city)
            time.sleep(3)
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
           city.replace(',', '').replace(' ', '-'),
            # timestamp in UTC
           datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')
        )
        with open(os.path.join(NUMBEO_DIR, filename), 'w') as f:
            f.write(html)

