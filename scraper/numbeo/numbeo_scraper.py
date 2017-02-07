from splinter import Browser
from selenium.webdriver.common.keys import Keys
import os
from scraper import rand_wait
from time import sleep


class NumbeoScraper(object):
    """ Scrapes numbeo.com for cost of living data
    """
    def get_html_for_city(self, city):
        with Browser('chrome') as b:
            # visit home page
            b.visit('https://www.numbeo.com/cost-of-living/')

            # fill search form with city
            rand_wait(b, '//*[@id="dispatch_form"]')
            search_form = b.driver.find_element_by_xpath('//*[@id="city_selector_city_id"]')
            search_form.send_keys(city)
            sleep(3)
            search_form.send_keys(Keys.TAB)
            #sleep(3)
            #search_form.send_keys(Keys.ENTER)
            #sleep()
            b.find_by_xpath('/html/body/div[6]/div[1]/button').first.click()
            sleep(100)

    def save_page(self, browser, city):
        with open('output.html', 'w') as f:
            f.write(browser.html.encode('utf-8'))


n = NumbeoScraper()
n.get_html_for_city('Denver, CO')
