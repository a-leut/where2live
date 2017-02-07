import os
import datetime
from time import sleep
from splinter import Browser
from selenium.webdriver.common.keys import Keys
from scraper import rand_wait_for_element
from scraper.config import NUMBEO_DIR

class NumbeoScraper(object):
    """ Scrapes numbeo.com for cost of living data
    """
    def __init__(self):
        if not os.path.isdir(NUMBEO_DIR):
            os.mkdir(NUMBEO_DIR)

    def get_html_for_city(self, city):
        with Browser('chrome') as b:
            # visit home page
            b.visit('https://www.numbeo.com/cost-of-living/')

            # fill search form with city
            rand_wait_for_element(b, '//*[@id="dispatch_form"]')
            search_form = b.driver.find_element_by_xpath('//*[@id="city_selector_city_id"]')
            search_form.send_keys(city)
            sleep(3)
            search_form.send_keys(Keys.TAB)
            b.find_by_xpath('/html/body/div[6]/div[1]/button').first.click()
            self.save_page(b, city)
            sleep(100)

    def save_page(self, browser, city):
        #filename = '{0}_[1}.html'.format(
        #    'hey'
        #    datetime.datetime.now().strftime('%m %d-%y_%H:%M')
        #)
        filename = city.strip()
        with open(os.path.join(NUMBEO_DIR, filename), 'w') as f:
            f.write(browser.html.encode('utf-8'))

n = NumbeoScraper()
n.get_html_for_city('Denver, CO')
