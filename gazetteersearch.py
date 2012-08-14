# -*- coding: utf-8 -*-
"""
/***************************************************************************
 gazetteerSearch
                                 A QGIS plugin
 Gazetteer Search plugin
                              -------------------
        begin                : 2012-07-21
        copyright            : (C) 2012 by Nathan Woodrow
        email                : woodrow.nathan@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import QFileInfo, QSettings, QTranslator, QCoreApplication, Qt
from PyQt4.QtGui import QDockWidget, QIcon, QAction
from gazetteersearchdialog import gazetteerSearchDialog
import resources_rc
from qgis.core import QgsApplication
from urllib2 import urlopen
from urllib import urlencode

from parsers.astun import AstunJson

class gazetteerSearch:

    def __init__(self, iface):
        self.dock = None
        self.astun = AstunJson()
        # Save reference to the QGIS interface
        self.iface = iface
        # Create the dialog and keep reference
        self.widget = gazetteerSearchDialog()
        self.widget.runSearch.connect(self.runSearch)
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/gazetteersearch"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]
       
        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/gazetteersearch_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
   

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/gazetteersearch/icon.png"), \
            u"Gazetteer Search", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Gazetteer Search", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Gazetteer Search",self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        if not self.dock:
            self.dock = QDockWidget("Gazzetteer Search", self.iface.mainWindow())
            self.dock.setWidget(self.widget)
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)
            self.widget.addGazetter(self.astun.name)
        else:
            self.dock.show()
            
    def runSearch(self, searchString):
        self.widget.clearResults()
        url, data = self.astun.getUrlAndData(searchString)
        params = urlencode(data)
        data = urlopen(url + "?" + params).read()
        results = self.astun.parseURLResults(data)
        for res in results:
            self.widget.addResult(res.description)
    