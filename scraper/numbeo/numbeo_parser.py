import os
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from scraper.settings import NUMBEO_DIR


def parse_cost_index(document_path):
    """ Returns a list containing cost of living data from a numbeo.com html
        file
    """
    with open(document_path, 'r', encoding='utf-8') as f:
        doc = f.read()
    soup = BeautifulSoup(doc, 'html.parser')
    index_table = soup.find('table', {'class': 'table_indices'})
    if index_table:
        rows = index_table.findChildren('tr')
        data = []
        for row in rows:
            tds = row.findAll('td')
            try:
                data.append(tds[1].text.strip())
            except:
                pass
        return data
    else:
        return None


def parse_all():
    """ Parses all the HTML files in the numbeo directory
    """
    data = []
    print('Parsing cost indices...')
    for path in tqdm(os.listdir(NUMBEO_DIR)):
        if path.endswith('.html'):
            index = parse_cost_index(os.path.join(NUMBEO_DIR, path))
            if index:
                index.append(path)
                data.append(index)
    print('Found indices in {0} / {1} files.'.format(
        len(os.listdir(NUMBEO_DIR)), len(data)
    ))
    df = pd.DataFrame(data)
    return df


def main():
    df = parse_all()
    print(df)
    df.to_csv(os.path.join(NUMBEO_DIR, 'cost_index.csv'))

if __name__ == '__main__':
    main()
