from urllib2 import urlopen
from urllib import urlencode

def getGazetteers():
    from ConfigParser import ConfigParser
    import os
    path = os.path.dirname(__file__)
    config = ConfigParser()
    config.read(os.path.join(path,'config.ini'))
    dictionary = {}
    for section in config.sections():
        dictionary[section] = {}
        for option in config.options(section):
            dictionary[section][option] = config.get(section, option)
    return dictionary

def perpareParams(params, query, **kwargs):
    new_params = params.copy()
    for key, value in params.items():
        if value == "##searchstring##":
            new_params[key] = query
            
    params = urlencode(new_params)       
    return params

def search(url, params):
    return urlopen(url + "?" + params).read()
