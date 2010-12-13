# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arbolbinario.ui'
#
# Created: Sun Dec 12 20:07:01 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 607)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 31))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.red = QtGui.QGridLayout(self.gridLayoutWidget)
        self.red.setObjectName(_fromUtf8("red"))
        self.texto = QtGui.QLineEdit(self.gridLayoutWidget)
        self.texto.setObjectName(_fromUtf8("texto"))
        self.red.addWidget(self.texto, 0, 0, 1, 1)
        self.botonagregar = QtGui.QPushButton(self.gridLayoutWidget)
        self.botonagregar.setObjectName(_fromUtf8("botonagregar"))
        self.red.addWidget(self.botonagregar, 0, 1, 1, 1)
        self.botonretirar = QtGui.QPushButton(self.gridLayoutWidget)
        self.botonretirar.setObjectName(_fromUtf8("botonretirar"))
        self.red.addWidget(self.botonretirar, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.barramenu = QtGui.QMenuBar(MainWindow)
        self.barramenu.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.barramenu.setObjectName(_fromUtf8("barramenu"))
        self.menuArchivo = QtGui.QMenu(self.barramenu)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        MainWindow.setMenuBar(self.barramenu)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menusalir = QtGui.QAction(MainWindow)
        self.menusalir.setObjectName(_fromUtf8("menusalir"))
        self.menuArchivo.addAction(self.menusalir)
        self.barramenu.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.menusalir, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.botonagregar.setText(QtGui.QApplication.translate("MainWindow", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.botonretirar.setText(QtGui.QApplication.translate("MainWindow", "Retirar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("MainWindow", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menusalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))

