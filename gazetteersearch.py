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
from PyQt4.QtCore import (QFileInfo, QSettings, QTranslator, 
                          QCoreApplication, Qt, QSizeF)
from PyQt4.QtGui import QDockWidget, QIcon, QAction, QTextDocument, QColor
from gazetteersearchdialog import gazetteerSearchDialog
from qgis.core import (QgsApplication, QgsMessageLog, QgsCoordinateReferenceSystem,
                       QgsRectangle, QgsCoordinateTransform)
from qgis.gui import QgsVertexMarker, QgsAnnotationItem

from importlib import import_module
from gazetteers import common
import resources_rc

log = lambda m: QgsMessageLog.logMessage(m,'Gazetteer')

class Result(object):
    def __init__(self,iface,description=None,x=None,y=None,zoom=None,epsg=None):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.description = unicode(description)
        self.x = float(x)
        self.y = float(y)
        self.zoom = int(zoom)
        self.epsg = int(epsg)
        self.marker = QgsVertexMarker(self.canvas)
        self.marker.setIconSize(20)
        self.marker.setPenWidth(3)
        self.marker.setIconType(QgsVertexMarker.ICON_CROSS)
        self.marker.setColor(QColor('green'))
        self._active = False
        self._visible = False
        self._xtrans = None
        self._ytrans = None

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self,value):
        if value == True:
            self._active = True
            self.marker.setColor(QColor('red'))
            self.marker.updateCanvas()
        else:
            self._active = False
            self.marker.setColor(QColor('green'))
            self.marker.updateCanvas()

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self,value):
        if value == True:
            if self.x is not None and self.y is not None:
                self._visible = True
                dest_crs = self.canvas.mapRenderer().destinationCrs()
                src_crs = QgsCoordinateReferenceSystem()
                src_crs.createFromEpsg(self.epsg)
                transform = QgsCoordinateTransform(src_crs, dest_crs)
                new_point = transform.transform(self.x, self.y)
                self._xtrans = new_point.x()
                self._ytrans = new_point.y()
                self.marker.setCenter(new_point)
                self.marker.show()
            else:
                self._visible = False
                raise ValueError("Can't show marker without x and y coordinates.")
        else:
            self._visible = False
            self.marker.hide()

    def unload(self):
        self.canvas.scene().removeItem(self.marker)
        self.marker = None

    def zoomTo(self):
        if self._xtrans is not None and self._ytrans is not None:
            r = QgsRectangle(self._xtrans,self._ytrans,self._xtrans,self._ytrans)
            self.canvas.setExtent(r)
            self.canvas.zoomScale(self.zoom)
            self.canvas.refresh()
        else:
            raise ValueError("Point does not have x and y coordinates")



class gazetteerSearch:
    def __init__(self, iface):
        self.dock = None
        self.results = []
        self.activeIndex = None
        # Save reference to the QGIS interface
        self.iface = iface
        self.iface.newProjectCreated.connect(self._hideMarker)
        self.iface.projectRead.connect(self._hideMarker)
        self.canvas = self.iface.mapCanvas()
        
        # Create the dialog and keep reference
        self.widget = gazetteerSearchDialog()
        self.widget.runSearch.connect(self.runSearch)
        self.widget.ui.clearButton.pressed.connect(self.clearResults)
        self.widget.zoomRequested.connect(self.zoomTo)
        self.widget.changeRequested.connect(self.changeSelected)
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
        for res in self.results:
            res.unload()
    
    def _hideMarker(self):
        for res in self.results:
            res.visible = False
    
    # run method that performs all the real work
    def run(self):
        if not self.dock:
            self.dock = QDockWidget("Gazetteer Search", self.iface.mainWindow())
            self.dock.setWidget(self.widget)
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)
            self.gazetteers = common.getGazetteers()
            for gazetter in self.gazetteers.iterkeys(): 
                self.widget.addGazetter(gazetter)
                
            if len(self.gazetteers) == 1:
                self.widget.hideGazetteers()
        else:
            self.dock.show()
            
    def runSearch(self, searchString, selectedGazetteer):
        self.clearResults()
        gazetteer_config = self.gazetteers[str(selectedGazetteer)]
        gazetteer = self.getGazetteerModule(gazetteer_config)
        url = common.prepareURL(gazetteer.url, gazetteer.params, searchString)
        data = common.search(url)
        
        try:
            results = list(gazetteer.parseRequestResults(data))
        except ValueError:
            self.results = []
            
        if len(results) == 0:
            self.widget.addError('No results found for "%s"' % searchString)
            
        for res in results:
            r = Result(self.iface, res.description, res.x, res.y, res.zoom, res.epsg)
            self.widget.addResult(r.description)
            r.index = self.widget.getListCount()-1
            r.visible = True
            self.results.append(r)
                        
    def clearResults(self):
        self.widget.clearResults()
        for res in self.results:
            res.unload()
        self.results = []
        self.activeIndex=None
            
    def getGazetteerModule(self, config):
        gazetteer_module = config['gazetteer']    
        imported_gazetteer = import_module('gazetteers.%s' % gazetteer_module)
        return imported_gazetteer
            
    def zoomTo(self, row):
        self.results[row-1].zoomTo()

    def changeSelected(self, row):
        if self.activeIndex is not None:
            self.results[self.activeIndex].active = False
        self.results[row-1].active = True
        self.activeIndex = row-1
