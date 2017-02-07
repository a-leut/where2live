import re

lines = []
states = {}

with open('state_codes.csv', 'r') as f:
    for l in f.readlines()[1:]:
        tk = l.split(',')
        states[tk[0]] = tk[1].strip()

with open('.\cities.csv', 'r') as f:
    with open('clean_cities.csv', 'w') as o:
        for l in f.readlines():
            new_line = re.sub('\[\d+\]', '', l).replace(',', ', ')
            for key in states.keys():
                if key in new_line:
                    tk = new_line.split(', ')
                    new_suffix = tk[1].replace(key, states[key])
                    new_line = tk[0] + ', ' + new_suffix
                    break
            o.write(new_line)
