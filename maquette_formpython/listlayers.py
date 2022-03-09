
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QAction, QMenu , QApplication, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog

from qgis.core import *
from qgis.gui import *
import qgis

import os

class Ui_Dialog(object):
    def __init__(self):
        self.iface = qgis.utils.iface
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,700,370).size()).expandedTo(Dialog.minimumSizeHint()))
        Dialog.setWindowTitle("Liste des couches de la fenêtre carte")

        self.ComboBox = QtWidgets.QComboBox(Dialog)
        self.ComboBox.setMinimumSize(QtCore.QSize(540, 25))
        self.ComboBox.setMaximumSize(QtCore.QSize(540, 25))
        self.ComboBox.setGeometry(QtCore.QRect(10, 10, 540,25))
        self.ComboBox.setObjectName("ComboBox")
        
        #Alimente la comboBox
        zList = self.iface.mapCanvas().layers()
        for i in zList : self.ComboBox.addItem(i.name())

        self.TextEdit = QtWidgets.QTextEdit(Dialog)
        self.TextEdit.setMinimumSize(QtCore.QSize(540, 300))
        self.TextEdit.setMaximumSize(QtCore.QSize(540, 300))
        self.TextEdit.setGeometry(QtCore.QRect(10, 50, 540,300))
        self.TextEdit.setObjectName("TextEdit")
        
        self.PushButton = QtWidgets.QPushButton(Dialog)
        self.PushButton.setGeometry(QtCore.QRect(560, 50, 130,20))
        self.PushButton.setObjectName("PushButton")
        self.PushButton.setText("Fermer")

        self.FileButton = QtWidgets.QPushButton(Dialog)
        self.FileButton.setGeometry(QtCore.QRect(560, 80, 130,20))
        self.FileButton.setObjectName("FileButton")
        self.FileButton.setText("Open file")

        self.DirButton = QtWidgets.QPushButton(Dialog)
        self.DirButton.setGeometry(QtCore.QRect(560, 110, 130,20))
        self.DirButton.setObjectName("DirButton")
        self.DirButton.setText("Open folder")
        
        self.printButton = QtWidgets.QPushButton(Dialog)
        self.printButton.setGeometry(QtCore.QRect(560, 140, 130,20))
        self.printButton.setObjectName("printButton")
        self.printButton.setText("Print baby !")


        self.initDir = os.path.dirname(__file__)

        self.PushButton.clicked.connect(Dialog.reject)
        self.FileButton.clicked.connect(self.openFile)
        self.DirButton.clicked.connect(self.openDir)
        self.printButton.clicked.connect(self.printMetadataLayer)
        
        self.ComboBox.currentIndexChanged.connect(Dialog.GetMetaData)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def GetMetaData(self, index='', layer=''):
        if not layer:
            icurrentIndex = self.ComboBox.currentIndex()
            layer = self.iface.mapCanvas().layers()[icurrentIndex]
        self.TextEdit.setText(f"{layer.htmlMetadata()}")
        
    def openFile(self):
        file = QFileDialog.getOpenFileName(None,"Fichier Shape :",self.initDir,"*.shp")
        layer = QgsVectorLayer(file[0], file[0], "ogr")
        self.GetMetaData(layer=layer)
        
    def openDir(self):
        rep = QFileDialog.getExistingDirectory(self, "Sélectionner un dossier", self.initDir, QFileDialog.ShowDirsOnly)
        QMessageBox.information(None, "Répertoire choisi", f"Répertoire [{rep}]")

    def printMetadataLayer(self):
        printer = QPrinter()
        printer.setPageSize(QPrinter.A4)
        printer.setOrientation(QPrinter.Portrait)
        printer.setOutputFormat(QPrinter.NativeFormat)
        printDialog = QPrintPreviewDialog(printer)
        zTitle = "Imprimer les métadonnées de la couche"
        printDialog.setWindowTitle(zTitle)
        printDialog.setWindowState(Qt.WindowNoState)
        printDialog.paintRequested.connect(self.TextEdit.print_)
        printDialog.exec_()