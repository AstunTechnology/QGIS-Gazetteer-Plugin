# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gazetteersearch.ui'
#
# Created: Fri Aug 17 10:11:22 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_gazetteerSearch(object):
    def setupUi(self, gazetteerSearch):
        gazetteerSearch.setObjectName(_fromUtf8("gazetteerSearch"))
        gazetteerSearch.resize(393, 452)
        self.gridLayout = QtGui.QGridLayout(gazetteerSearch)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(gazetteerSearch)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 4)
        self.label = QtGui.QLabel(gazetteerSearch)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.searchEdit = QtGui.QLineEdit(gazetteerSearch)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.gridLayout.addWidget(self.searchEdit, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(gazetteerSearch)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.gazzetterCombo = QtGui.QComboBox(gazetteerSearch)
        self.gazzetterCombo.setObjectName(_fromUtf8("gazzetterCombo"))
        self.gridLayout.addWidget(self.gazzetterCombo, 2, 1, 1, 1)
        self.line = QtGui.QFrame(gazetteerSearch)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 3, 0, 1, 4)
        self.resultsList = QtGui.QListWidget(gazetteerSearch)
        self.resultsList.setObjectName(_fromUtf8("resultsList"))
        self.gridLayout.addWidget(self.resultsList, 4, 0, 1, 4)
        self.goButton = QtGui.QPushButton(gazetteerSearch)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goButton.sizePolicy().hasHeightForWidth())
        self.goButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.goButton.setFont(font)
        self.goButton.setObjectName(_fromUtf8("goButton"))
        self.gridLayout.addWidget(self.goButton, 1, 2, 2, 1)

        self.retranslateUi(gazetteerSearch)
        QtCore.QObject.connect(self.searchEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.goButton.click)
        QtCore.QMetaObject.connectSlotsByName(gazetteerSearch)

    def retranslateUi(self, gazetteerSearch):
        gazetteerSearch.setWindowTitle(QtGui.QApplication.translate("gazetteerSearch", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("gazetteerSearch", "Where would you like to go today?", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("gazetteerSearch", "Search for:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("gazetteerSearch", "Gazetteer:", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setText(QtGui.QApplication.translate("gazetteerSearch", "Go!", None, QtGui.QApplication.UnicodeUTF8))

