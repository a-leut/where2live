import re

lines = []

with open('cities.csv', 'r') as f:
    with open('clean_cities.csv', 'w') as o:
        for l in f.readlines():
            o.write(re.sub('\[\d+\]', '', l).replace(',', ', '))
