from splinter import Browser
from indexer.settings import CITIES_FILE, GLASSDOOR_DIR
from indexer.item_indexer import ItemIndexer
from indexer.util import rand_wait_for_element


class GlassdoorIndexer(ItemIndexer):
    """ Indexes salary pages from glassdoor.com website
    """
    def get_html_for_item(self, item):
        """ Scrapes the site for an item (city) and stores the result page
        """
        with Browser(self.browser_type) as browser:
            browser.visit('https://www.glassdoor.com/Salaries/')

            search_box = browser.find_by_xpath('//*[@id="sc.location"]')
            search_box.click()


def main():
    with open(CITIES_FILE, 'r') as f:
        cities = f.read().split('\n')[1:]
    idx = GlassdoorIndexer('chrome', GLASSDOOR_DIR)
    idx.get_html_for_item('Denver, CO')

if __name__ == '__main__':
    main()
