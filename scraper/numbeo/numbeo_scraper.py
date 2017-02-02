from splinter import Browser
from scraper import rand_wait
from time import sleep


class NumbeoScraper(object):
    """ Scrapes numbeo.com for cost of living data
    """
    def get_html_for_city(self, city):
        with Browser('chrome') as browser:
            # visit home page
            browser.visit('https://www.numbeo.com/cost-of-living/')

            # fill search form with city
            search_xp = '//*[@id="dispatch_form"]'
            rand_wait(browser, search_xp)
            search_form = browser.find_by_xpath(search_xp).first
            search_form.find_by_xpath('//*[@id="city_selector_city_id"]').fill('booty')
            sleep(100)

n = NumbeoScraper()
n.get_html_for_city('c')
