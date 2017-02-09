import datetime
import time
import random


def utc_timestamp():
    """ Return system time in UTC formatted to include up to seconds
    """
    return datetime.datetime.fromtimestamp(time.time()).\
        strftime('%Y-%m-%d_%H-%M-%S')


def rand_wait_for_element(browser, xpath, additional_max=0):
    """ Waits for xpath and adds random wait of 1 to additional_max sec
    """
    present = browser.is_element_present_by_xpath(xpath)
    if present:
        time.sleep(random.random() * additional_max)
        return True
    else:
        return False