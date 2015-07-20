from __future__ import division
from collections import namedtuple
from qgis.core import (QgsRectangle, QgsCoordinateTransform, QgsCoordinateReferenceSystem, QgsScaleCalculator)
import json

url = "http://t0.ads.astuntechnology.com/open/search/osopennames/"
params = {
    'q': '##searchstring##'
}


def parseRequestResults(data, iface=None):
    feats = json.loads(data)
    for feat in feats.get('features', []):
        result = namedtuple('Result', ['description', 'x', 'y', 'zoom', 'epsg'])
        result.description = feat['properties']['search_full']
        result.x = feat['geometry']['coordinates'][0]
        result.y = feat['geometry']['coordinates'][1]
        result.epsg = 4326
        result.zoom = calc_scale(feat['bbox'], iface.mapCanvas().mapRenderer()) if iface else 50000
        yield result


def calc_scale(bbox, map_renderer):
    coord_transform = QgsCoordinateTransform(
        QgsCoordinateReferenceSystem(4326),
        QgsCoordinateReferenceSystem(27700)
    )
    # As we are using the QgsScaleCalculator to determine the scale we need to
    # create a standard bounding box to calculate the scale for the width and a
    # bounding box on it's side to calculate the scale to fit the height
    width_bbox = coord_transform.transform(QgsRectangle(bbox[0], bbox[1], bbox[2], bbox[3]))
    height_bbox = coord_transform.transform(QgsRectangle(bbox[1], bbox[0], bbox[3], bbox[2]))
    scale_calc = QgsScaleCalculator(map_renderer.outputDpi())
    scale = max(
        scale_calc.calculate(width_bbox, map_renderer.width()),
        scale_calc.calculate(height_bbox, map_renderer.height())
    )
    return scale * 1.1


if __name__ == '__main__':
    with open('astunosopennames.json') as f:
        content = unicode(f.read(), 'UTF-8')
        results = list(parseRequestResults(content))
        for item in results:
            print item.description, item.x, item.y, item.zoom, item.epsg
