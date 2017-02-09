from splinter import Browser


class GlassdoorScraper(object):
    """ Scrapes data from glassdoor.com website
    """
    def __init__(self, cities=[]):
        self._city_results = dict.fromkeys(cities, None)
        print(self._city_results)

    def get_city_prices(self):
        self.scrape_site()
        return self._city_results

    def scrape_site(self):
        """ Scrapes the site for each city and stores the salary in the results
        """
        with Browser('chrome') as browser:
            browser.visit('https://www.glassdoor.com/Salaries/software-engineer-salary-SRCH_KO0,17.htm')

            search_box = browser.find_by_xpath('//*[@id="sc.location"]')
            search_box.click()
