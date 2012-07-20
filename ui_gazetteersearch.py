# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gazetteersearch.ui'
#
# Created: Sat Jul 21 00:48:30 2012
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
        self.lineEdit = QtGui.QLineEdit(gazetteerSearch)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(gazetteerSearch)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(gazetteerSearch)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.line = QtGui.QFrame(gazetteerSearch)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 3, 0, 1, 4)
        self.listWidget = QtGui.QListWidget(gazetteerSearch)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 4, 0, 1, 4)
        self.searchButton = QtGui.QPushButton(gazetteerSearch)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.gridLayout.addWidget(self.searchButton, 1, 2, 2, 1)

        self.retranslateUi(gazetteerSearch)
        QtCore.QMetaObject.connectSlotsByName(gazetteerSearch)

    def retranslateUi(self, gazetteerSearch):
        gazetteerSearch.setWindowTitle(QtGui.QApplication.translate("gazetteerSearch", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("gazetteerSearch", "Where would you like to go today?", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("gazetteerSearch", "Search for:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("gazetteerSearch", "Gazzetter:", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("gazetteerSearch", "Go!", None, QtGui.QApplication.UnicodeUTF8))

