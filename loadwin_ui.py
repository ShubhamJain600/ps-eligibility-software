# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\LoadWin.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadWin(object):
    def setupUi(self, LoadWin):
        LoadWin.setObjectName("LoadWin")
        LoadWin.resize(401, 94)
        LoadWin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label = QtWidgets.QLabel(LoadWin)
        self.label.setGeometry(QtCore.QRect(10, 10, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(LoadWin)
        QtCore.QMetaObject.connectSlotsByName(LoadWin)

    def retranslateUi(self, LoadWin):
        _translate = QtCore.QCoreApplication.translate
        LoadWin.setWindowTitle(_translate("LoadWin", "Loading"))
        self.label.setText(_translate("LoadWin", "Loading files..."))
