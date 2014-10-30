# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gazetteersearch.ui'
#
# Created: Fri Aug 15 11:34:36 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_gazetteerSearch(object):
    def setupUi(self, gazetteerSearch):
        gazetteerSearch.setObjectName(_fromUtf8("gazetteerSearch"))
        gazetteerSearch.resize(674, 233)
        self.gridLayout = QtGui.QGridLayout(gazetteerSearch)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(gazetteerSearch)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 5)
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
        self.gridLayout.addWidget(self.goButton, 1, 4, 1, 1)
        self.clearButton = QtGui.QPushButton(gazetteerSearch)
        self.clearButton.setCheckable(False)
        self.clearButton.setAutoRepeat(False)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.gridLayout.addWidget(self.clearButton, 2, 4, 1, 1)
        self.searchEdit = QtGui.QLineEdit(gazetteerSearch)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.gridLayout.addWidget(self.searchEdit, 1, 1, 1, 1)
        self.resultsList = QtGui.QListWidget(gazetteerSearch)
        self.resultsList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.resultsList.setObjectName(_fromUtf8("resultsList"))
        self.gridLayout.addWidget(self.resultsList, 4, 1, 1, 4)
        self.line = QtGui.QFrame(gazetteerSearch)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 3, 1, 1, 4)
        self.gazzetterCombo = QtGui.QComboBox(gazetteerSearch)
        self.gazzetterCombo.setObjectName(_fromUtf8("gazzetterCombo"))
        self.gridLayout.addWidget(self.gazzetterCombo, 6, 1, 1, 1)
        self.label_2 = QtGui.QLabel(gazetteerSearch)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)

        self.retranslateUi(gazetteerSearch)
        QtCore.QObject.connect(self.searchEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.goButton.click)
        QtCore.QMetaObject.connectSlotsByName(gazetteerSearch)

    def retranslateUi(self, gazetteerSearch):
        gazetteerSearch.setWindowTitle(_translate("gazetteerSearch", "Form", None))
        self.label_3.setText(_translate("gazetteerSearch", "Search for:", None))
        self.goButton.setText(_translate("gazetteerSearch", "Go!", None))
        self.clearButton.setText(_translate("gazetteerSearch", "Clear", None))
        self.label_2.setText(_translate("gazetteerSearch", "Gazetteer:", None))
