from collections import namedtuple
from xml.etree import ElementTree
from common import text, pretty_join

url = "http://where.yahooapis.com/v1/places.q('##searchstring##');count=25"
params = {
    'appid': 's80LwDXV34EAC3zK0dh9k43ZuDaDjXPqzgPK3kNOhn0AJMD6l1dIOS0kqiKBYnhFjESgLAedBIK.DCHgup8F5Kvvcd9y9CY-'
}


def parseRequestResults(data, iface=None):
    def schema(name):
        return './/{http://where.yahooapis.com/v1/schema.rng}%s' % name

    tree = ElementTree.fromstring(data.encode('UTF-8'))
    for item in tree.findall(schema('place')):
        result = namedtuple('Result', ['description', 'x', 'y', 'zoom', 'epsg'])
        desc = [text(item, schema('name')),
                text(item, schema('admin1')),
                text(item, schema('admin2')),
                text(item, schema('country'))]
        result.description = pretty_join(", ", desc)
        centroid = item.find(schema('centroid'))
        result.x = float(text(centroid, schema('longitude')))
        result.y = float(text(centroid, schema('latitude')))
        result.zoom = 50000
        result.epsg = 4326
        yield result

if __name__ == '__main__':
    with open('yahoo.xml') as f:
        content = unicode(f.read(), 'UTF-8')
        results = list(parseRequestResults(content))
        for item in results:
            print item.description
