# -*- coding: utf-8 -*-
"""
/***************************************************************************
 gazetteerSearchDialog
                                 A QGIS plugin
 Gazetteer
Search plugin
                             -------------------
        begin                : 2012-07-21
        copyright            : (C) 2012,2013 by Nathan Woodrow, Rudi von Staden
        email                : rudivs@gmail.com
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

from PyQt4 import QtCore, QtGui
from ui_gazetteersearch import Ui_gazetteerSearch
import resources_rc

class gazetteerSearchDialog(QtGui.QDialog):
    runSearch = QtCore.pyqtSignal(str, str)
    zoomRequested = QtCore.pyqtSignal(int)
    changeRequested = QtCore.pyqtSignal(int)
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_gazetteerSearch()
        self.ui.setupUi(self)
        self.ui.goButton.pressed.connect(self._doSearch)
        self.ui.resultsList.itemActivated.connect(self._zoomTo)
        self.ui.resultsList.currentItemChanged.connect(self._itemChanged)
    
    def addGazetter(self, gazetter):
        self.ui.gazzetterCombo.addItem(gazetter)
    
    def selectedGazetteer(self):
        return self.ui.gazzetterCombo.currentText()
        
    def addResult(self, name):
        self.hasErrors = False
        item = QtGui.QListWidgetItem(name)
        self.ui.resultsList.addItem(item)

    def getListCount(self):
        return self.ui.resultsList.count()

    def getListIndex(self):
        return self.ui.resultsList.currentRow()

    def clearResults(self):
        self.hasErrors = False
        self.ui.resultsList.clear()
        
    def hideGazetteers(self):
        self.ui.gazzetterCombo.hide()
        self.ui.label_2.hide()
        
    def _doSearch(self):
        self.clearResults()
        self.runSearch.emit(self.ui.searchEdit.text(), self.selectedGazetteer())
    
    def _zoomTo(self, item):
        if self.hasErrors:
            return
        else:
            self.zoomRequested.emit(self.ui.resultsList.currentRow())

    def _itemChanged(self,currentItem,previousItem):
        if self.hasErrors:
            return
        else:
            self.changeRequested.emit(self.ui.resultsList.currentRow())
     
    def addError(self, text):
        self.hasErrors = True
        item = QtGui.QListWidgetItem(text)
        item.setIcon(QtGui.QIcon(self.plugin_dir + "/warning.png"))
        item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter )
        item.setForeground(QtCore.Qt.red)
        self.ui.resultsList.addItem(item)   
