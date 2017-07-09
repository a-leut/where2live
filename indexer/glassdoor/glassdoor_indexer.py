import time
from splinter import Browser

from indexer.settings import CITIES_FILE, GLASSDOOR_DIR
from indexer.item_indexer import ItemIndexer
from indexer.util import rand_wait_for_element
from selenium.webdriver.common.keys import Keys

class GlassdoorIndexer(ItemIndexer):
    """ Indexes salary pages from glassdoor.com website
    """
    def get_html_for_item(self, item):
        """ Scrapes the site for an item (city) and stores the result page
        """
        with Browser('phantomjs') as browser:
            job = 'Software Engineer'
            #job, city = 'Nurse', 'Denver'#item
            browser.visit('https://www.glassdoor.com/Salaries/')
            city_box = browser.find_by_id('LocationSearch')
            #for _ in range(15):
            #    city_box.type(Keys.BACKSPACE)
            city_box.type(item)
            time.sleep(1)
            browser.type('sc.keyword', job)
            time.sleep(1.5)
            button = browser.find_by_id('HeroSearchButton')
            button.click()
            #browser.find_by_xpath('//body').type(Keys.CONTROL + Keys.TAB)
            browser.windows.current = browser.windows[1]
           #browser.find_by_tag('body').send_keys()
            #salaries = browser.find_by_xpath('//*[@id="TopNav"]/nav/div[2]/ul[2]/li[4]/a')
            #salaries.click()
            # time.sleep(1000000)
            return str(browser.html)


def main():
    with open(CITIES_FILE, 'r') as f:
        cities = f.read().split('\n')[1:]
    idx = GlassdoorIndexer('chrome', GLASSDOOR_DIR)
    idx.index_items(cities)
    #txt = idx.get_html_for_item('Denver, CO')
    #open('1.html', 'w', encoding='utf-8').write(txt)

if __name__ == '__main__':
    main()
