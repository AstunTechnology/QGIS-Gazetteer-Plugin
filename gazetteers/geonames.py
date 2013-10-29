from collections import namedtuple
from xml.etree import ElementTree
from common import text, pretty_join

url = "http://api.geonames.org/search"
params = {
    'q': '##searchstring##',
    'maxRows': '25',
    'style': 'LONG',
    'lang': 'en',
    'username': 'astuntech_qgis_gaz'
}


def parseRequestResults(data):
    tree = ElementTree.fromstring(data)
    for item in tree.findall('geoname'):
        result = namedtuple('Result', ['description', 'x', 'y', 'zoom', 'epsg'])
        desc = [text(item, 'name'), text(item, 'countryName')]
        result.description = pretty_join(", ", desc)
        result.x = float(text(item, 'lng'))
        result.y = float(text(item, 'lat'))
        result.zoom = 50000
        result.epsg = 4326
        yield result

if __name__ == '__main__':
    with open('geonames.xml') as f:
        results = list(parseRequestResults(f.read()))
        for item in results:
            print item.description
