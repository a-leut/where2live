import splinter

class GlassdoorScraper(object):
    """ Scrapes data from glassdoor.com website
    """
    def __init__(self):
        self._s = splinter.Browser('phantomjs')

    def login(self):
        pass
