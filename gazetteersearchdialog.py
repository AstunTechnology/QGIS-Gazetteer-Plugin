# -*- coding: utf-8 -*-
"""
/***************************************************************************
 gazetteerSearchDialog
                                 A QGIS plugin
 Gazetteer
Search plugin
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

from PyQt4 import QtCore, QtGui
from ui_gazetteersearch import Ui_gazetteerSearch
from functools import partial
# create the dialog for zoom to point
class gazetteerSearchDialog(QtGui.QDialog):
    runSearch = QtCore.pyqtSignal(str)
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_gazetteerSearch()
        self.ui.setupUi(self)
        self.ui.goButton.pressed.connect(self._doSearch)
    
    def addGazetter(self, gazetter):
        self.ui.gazzetterCombo.addItem(gazetter)
        
    def addResult(self, name):
        self.ui.resultsList.addItem(QtGui.QListWidgetItem(name))

    def clearResults(self):
        self.ui.resultsList.clear()
        
    def _doSearch(self):
        self.runSearch.emit(self.ui.searchEdit.text())
        