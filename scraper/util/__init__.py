import datetime
import time


def utc_timestamp():
    """ Return system time in UTC formatted to include up to seconds
    """
    return datetime.datetime.fromtimestamp(time.time()).\
        strftime('%Y-%m-%d_%H-%M-%S')
