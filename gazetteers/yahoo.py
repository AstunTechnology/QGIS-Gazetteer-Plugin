from collections import namedtuple
from xml.etree import ElementTree

url = "http://where.yahooapis.com/v1/places.q('##searchstring##');count=25"
params = {
    'appid': 's80LwDXV34EAC3zK0dh9k43ZuDaDjXPqzgPK3kNOhn0AJMD6l1dIOS0kqiKBYnhFjESgLAedBIK.DCHgup8F5Kvvcd9y9CY-'
}


def parseRequestResults(data):
    def schema(name):
        return './/{http://where.yahooapis.com/v1/schema.rng}%s' % name

    tree = ElementTree.fromstring(data)
    for item in tree.findall(schema('place')):
        result = namedtuple('Result', ['description', 'x', 'y', 'zoom', 'epsg'])
        result.description = "%s, %s" % (item.find(schema('name')).text,
                                         item.find(schema('country')).text)
        centroid = item.find(schema('centroid'))
        result.x = float(centroid.find(schema('longitude')).text)
        result.y = float(centroid.find(schema('latitude')).text)
        result.zoom = 50000
        result.epsg = 4326
        yield result

if __name__ == '__main__':
    with open('yahoo.xml') as f:
        results = list(parseRequestResults(f.read()))
        for item in results:
            print item.description
