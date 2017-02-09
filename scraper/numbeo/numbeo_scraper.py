import time
import splinter
from selenium.webdriver.common.keys import Keys
from scraper.settings import CITIES_FILE, NUMBEO_DIR
from scraper.item_scraper import ItemScraper
from scraper.util import rand_wait_for_element


class NumbeoScraper(ItemScraper):
    """ Scrapes numbeo.com for cost of living data
    """
    def get_html_for_item(self, item):
        """ Launch browser, search for item (a city) on numbeo, and return html
        """
        with splinter.Browser(self.browser_type) as b:
            # Visit home page
            b.visit('https://www.numbeo.com/cost-of-living/')
            # Fill search form with city
            rand_wait_for_element(b, '//*[@id="dispatch_form"]')
            search_form = b.driver.find_element_by_xpath('//*[@id="city_selector_city_id"]')
            search_form.send_keys(item)
            time.sleep(5)
            search_form.send_keys(Keys.TAB)
            # Close signup popup if exists
            try:
                b.find_by_xpath('/html/body/div[6]/div[1]/button').first.click()
            except splinter.exceptions.ElementDoesNotExist:
                pass
            # Return search result
            return str(b.html)


def main():
    with open(CITIES_FILE, 'r') as f:
        cities = f.read().split('\n')[1:]
    scraper = NumbeoScraper('phantomjs', NUMBEO_DIR)
    scraper.scrape_items(cities)

if __name__ == '__main__':
    main()
