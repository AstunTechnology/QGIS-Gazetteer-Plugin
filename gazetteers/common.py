from urllib2 import urlopen
from urllib import urlencode
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *

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

def getProxy():
  # Adaption by source of "Plugin Installer - Version 1.0.10" 
  proxy = None
  settings = QSettings()
  settings.beginGroup("proxy")
  if settings.value("/proxyEnabled").toBool():
    proxy = QNetworkProxy()
    proxyType = settings.value( "/proxyType", QVariant(0)).toString()
    #if len(args)>0 and settings.value("/proxyExcludedUrls").toString().contains(args[0]):
    #  proxyType = "NoProxy"
    if proxyType in ["1","Socks5Proxy"]: proxy.setType(QNetworkProxy.Socks5Proxy)
    elif proxyType in ["2","NoProxy"]: proxy.setType(QNetworkProxy.NoProxy)
    elif proxyType in ["3","HttpProxy"]: proxy.setType(QNetworkProxy.HttpProxy)
    elif proxyType in ["4","HttpCachingProxy"] and QT_VERSION >= 0X040400: proxy.setType(QNetworkProxy.HttpCachingProxy)
    elif proxyType in ["5","FtpCachingProxy"] and QT_VERSION >= 0X040400: proxy.setType(QNetworkProxy.FtpCachingProxy)
    else: proxy.setType(QNetworkProxy.DefaultProxy)
    proxy.setHostName(settings.value("/proxyHost").toString())
    proxy.setPort(settings.value("/proxyPort").toUInt()[0])
    proxy.setUser(settings.value("/proxyUser").toString())
    proxy.setPassword(settings.value("/proxyPassword").toString())
  settings.endGroup()
  return proxy
