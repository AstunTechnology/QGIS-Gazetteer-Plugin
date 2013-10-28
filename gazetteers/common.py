from urllib2 import urlopen
from urllib import urlencode, quote
from qgis.core import QgsMessageLog

def getGazetteers():
    from ConfigParser import ConfigParser
    import os
    path = os.path.dirname(__file__)
    config = ConfigParser()
    config.read(os.path.join(path,'config.ini'))
    try:
        # Use OrderedDict if available so we maintain the section order and
        # hence the order of the entries in the list box
        from collections import OrderedDict
        d = OrderedDict()
    except:
        d = {}
    for section in config.sections():
        d[section] = {}
        for option in config.options(section):
            d[section][option] = config.get(section, option)
    return d

def prepareParams(params, query, **kwargs):
    new_params = params.copy()
    for key, value in params.items():
        if value == "##searchstring##":
            new_params[key] = query

    params = urlencode(new_params)
    return params

def prepareURL(url, params, query):
    params = prepareParams(params, query)
    newurl = url + "?" + params
    return newurl.replace("##searchstring##", quote(str(query)))

def search(url):
    QgsMessageLog.logMessage("URL:" + url, "Gazetteer")
    return urlopen(url).read()
