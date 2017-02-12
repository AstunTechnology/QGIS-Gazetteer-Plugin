from PyQt4.QtCore import QUrl
from PyQt4.QtCore import Qt
from PyQt4.QtNetwork import QNetworkRequest, QNetworkReply
from qgis.core import QgsMessageLog
from qgis.core import QgsNetworkAccessManager
from urllib import urlencode, quote

import cgi

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

def search(url, callback):
    QgsMessageLog.logMessage("URL:" + url, "Gazetteer")

    def requestFinished(reply):
        # Disconnect from the signal
        networkAccessManager = QgsNetworkAccessManager.instance()
        networkAccessManager.finished.disconnect(requestFinished)
        # Handle the reply
        if reply.error() != QNetworkReply.NoError:
            QgsMessageLog.logMessage("Network error #{0}: {1}".format(reply.error(), reply.errorString()), "Gazetteer")
            callback(u'')
        else:
            charset = 'UTF-8'
            try:
                _, params = cgi.parse_header(reply.header(QNetworkRequest.ContentTypeHeader))
                charset = params['charset']
            except:
                pass
            QgsMessageLog.logMessage("charset: " + charset, "Gazetteer")
            data = unicode(reply.readAll(), charset)
            print 'requestFinished, data: %s' % data
            reply.deleteLater()
            callback(data)

    networkAccessManager = QgsNetworkAccessManager.instance()
    networkAccessManager.finished.connect(requestFinished)
    networkAccessManager.get(QNetworkRequest(QUrl(url)))


def text(item, xpath):
    """ Return the text associated with a matched ElementTree node """
    return item.findtext(xpath, '')


def pretty_join(sep, items):
    """ Joins a list of items on sep[arator] discarding any Falsey values """
    return sep.join([i for i in items if i])
