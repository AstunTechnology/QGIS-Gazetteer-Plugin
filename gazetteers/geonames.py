from collections import namedtuple
from xml.etree import ElementTree

url = "http://api.geonames.org/search"
params = {
            'q': '##searchstring##',
            'maxRows': '6',
            'style': 'LONG',
            'lang':'es',
            'username':'demo'
          }
    
def parseRequestResults(data):
    tree = ElementTree.fromstring(data)
    for item in tree.findall('geoname'):
        result = namedtuple('Result',['description','x','y','zoom', 'epsg'])
        result.description = item.find('name').text
        result.x = float(item.find('lat').text)
        result.y = float(item.find('lng').text)
        result.zoom = 200
        result.epsg = 27700 
        yield result
         
if __name__ == '__main__':
    f = open('test_geonames.xml')
    results = list(parseRequestResults(f.read()))
    for item in results:
        print item.description