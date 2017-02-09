import os
import errno
import random
import time
from indexer.util import utc_timestamp


class ItemIndexer(object):
    """ Base class to index a website and download some html pages. Enumerates
        an input list and runs some action per input.
    """
    def __init__(self, browser_type, log_dir, force_reset=False):
        self.base_dir = log_dir
        self.log_file = os.path.join(
            log_dir, '{0}_log.txt'.format(self.__class__.__name__)
        )
        self.browser_type = browser_type
        # Make sure output dirs are set up
        try:
            os.makedirs(log_dir)
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(log_dir):
                pass
            else:
                raise
        # Delete tracked log if force reset
        if force_reset:
            try:
                os.remove(self.log_file)
            except OSError:
                pass
        # Create new tracked log if it doesnt exist
        if not os.path.isfile(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write('# {0} log\n# Started: {1}\n'.
                        format(self.__class__.__name__, utc_timestamp()))

    def index_items(self, target_items):
        """ Search for list of items on a site and save output to dir
        """
        # Find which items are already indexed from log
        with open(self.log_file, 'r') as f:
            log_lines = f.readlines()[2:]
        indexed_indems = [l.strip() for l in log_lines]
        new_items = set(target_items).difference(indexed_indems)
        new_items.discard('')  # newline not a city
        total_new = len(new_items)
        while len(new_items) > 0:
            # Choose random item
            new_item = random.choice(tuple(new_items))
            print('Using {0} for {1} - {2}/{3}'.format(
                self.__class__.__name__, new_item,
                total_new - len(new_items) + 1, total_new
            ))
            # Save html for item
            html = self.get_html_for_item(new_item)
            self.save_page(html, new_item)
            with open(self.log_file, 'a') as f:
                f.write('{0}\n'.format(new_item))
            new_items.discard(new_item)
            # Wait patiently to re-index
            time.sleep(random.randrange(4, 20))
        print('All items indexed, complete!')

    def save_page(self, html, item):
        filename = '{0}_{1}.html'.format(
            self.clean_item_name(item), utc_timestamp()
        )
        p = os.path.join(self.base_dir, filename)
        with open(p, 'w', encoding='utf-8') as out:
            out.write(html)

    def clean_item_name(self, item_name):
        """" Cleans an item name to be used as a filename
        """
        return item_name.replace(',', '').replace(' ', '-')

    def get_html_for_item(self, item):
        """ Launch browser, get page for item and, and return html
        """
        raise NotImplementedError('Not implemented.')
