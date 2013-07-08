from collections import namedtuple
from xml.etree import ElementTree

url = "http://api.geonames.org/search"
params = {
          'q':"##searchstring##",
          'maxRows': '200',
          'style': 'LONG',
          'lang': 'en',
          'fuzzy': '0.75',
          'username': 'rudivs',
          'country': ['ZA','SZ','LS','NA','BW','ZW','MZ'],
          'countryBias': 'ZA'
         }
    
def parseRequestResults(data):
    tree = ElementTree.fromstring(data)
    for item in tree.findall('geoname'):
        result = namedtuple('Result',['description','x','y','zoom', 'epsg'])
        result.description = unicode(item.find('name').text)
        result.x = float(item.find('lng').text)
        result.y = float(item.find('lat').text)
        result.zoom = 50000
        result.epsg = 4326 
        yield result
         
if __name__ == '__main__':
    f = open('test_geonames.xml')
    results = list(parseRequestResults(f.read()))
    for item in results:
        print item.description
