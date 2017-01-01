import json

def get_cities():
    """ Loads cities.json and returns list of cities
    """
    result = []
    with open('cities.json', 'r') as f:
        d = json.loads(f.read())
        for row in d['result']:
            result.append('%s, %s' % (row['City'], row['State']))
    return result
