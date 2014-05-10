from collections import namedtuple
from xml.etree import ElementTree

url = "http://nominatim.openstreetmap.org/search"
params = {
    'q': '##searchstring##',
    'limit': 50,
    'format': 'xml',
    'addressdetails': 1
}


def parseRequestResults(data):
    tree = ElementTree.fromstring(data.encode('UTF-8'))
    for place in tree.iter('place'):
        result = namedtuple('Result', ['description', 'x', 'y', 'zoom', 'epsg'])
        result.description = place.attrib['display_name']
        result.x = float(place.attrib['lon'])
        result.y = float(place.attrib['lat'])
        result.zoom = 50000
        result.epsg = 4326
        yield result

if __name__ == '__main__':
    with open('nominatim.xml') as f:
        content = unicode(f.read(), 'UTF-8')
        results = list(parseRequestResults(content))
        for item in results:
            print item.description
