""" Cleans a list of most populous cities copied from wikipedia for use as
    terms
"""
import re

lines = []
states = {}

# read in state names / postal codes
with open('state_codes.csv', 'r') as f:
    for l in f.readlines()[1:]:
        tk = l.split(',')
        states[tk[0]] = tk[1].strip()

# clean wikipedia data
with open('.\cities.csv', 'r') as f:
    with open('clean_cities.csv', 'w') as o:
        for l in f.readlines():
            # remove citations
            new_line = re.sub('\[\d+\]', '', l).replace(',', ', ')
            # change state for postal codes
            for key in states.keys():
                if key in new_line:
                    tk = new_line.split(', ')
                    new_suffix = tk[1].replace(key, states[key])
                    new_line = tk[0] + ', ' + new_suffix
                    break
            o.write(new_line)
