
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QAction, QMenu , QApplication, QMessageBox, QFileDialog
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog

from PyQt5.QtGui import QIcon

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

        self.OpenFile = QtWidgets.QPushButton(Dialog)
        self.OpenFile.setMinimumSize(QtCore.QSize(130, 20))
        self.OpenFile.setMaximumSize(QtCore.QSize(130, 20))
        self.OpenFile.setGeometry(QtCore.QRect(560, 120, 130,20))
        self.OpenFile.setObjectName("OpenFile")
        self.OpenFile.setText("Ouvrir fichier")

        self.OpenFolder = QtWidgets.QPushButton(Dialog)
        self.OpenFolder.setMinimumSize(QtCore.QSize(130, 20))
        self.OpenFolder.setMaximumSize(QtCore.QSize(130, 20))
        self.OpenFolder.setGeometry(QtCore.QRect(560, 150, 130,20))
        self.OpenFolder.setObjectName("OpenFolder")
        self.OpenFolder.setText("Ouvrir répertoire")

        self.PrintData = QtWidgets.QPushButton(Dialog)
        self.PrintData.setMinimumSize(QtCore.QSize(130, 20))
        self.PrintData.setMaximumSize(QtCore.QSize(130, 20))
        self.PrintData.setGeometry(QtCore.QRect(560, 180, 130,20))
        self.PrintData.setObjectName("PrintData")
        self.PrintData.setText("Imprimer")

        self.OpenFile.clicked.connect(Dialog.MyOpenFile)
        self.OpenFolder.clicked.connect(Dialog.MyOpenFolder)
        self.PrintData.clicked.connect(Dialog.MyPrintData)

        self.PushButton.clicked.connect(Dialog.reject)
        
        self.ComboBox.currentIndexChanged.connect(Dialog.GetMetaData)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #self.GetMetaData()        

    def MyOpenFile(self):
        #Ouverture de la boite de dialogue Fichiers
        InitDir = os.path.dirname(__file__) 
        TypeList = "Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)"
        fileName = QFileDialog.getOpenFileName(None,"Fichier Shape :",InitDir,TypeList)
        filemess = "j'ai sélectionné le fichier : " + str(fileName) if fileName != "" else "Pas de fichier sélectionné !" 
        QMessageBox.information(None,"Fichiers :", filemess)
        return 
        
    def MyOpenFolder(self):
        #Ouverture de la boite de dialogue Fichiers
        InitDir = "D:\\DIVERS" 
        inputDir = QFileDialog.getExistingDirectory(self, "Sélectionner un dossier", InitDir, QFileDialog.ShowDirsOnly|QFileDialog.DontResolveSymlinks)
        filemess = "j'ai sélectionné le répertoire : " + str(inputDir) if inputDir != "" else "Pas de répertoire sélectionné !" 
        QMessageBox.information(None,"Répertoire :", filemess)
        return 

    def MyPrintData(self):
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
       return 

    def GetMetaData(self):
        #Choix d'une couche dans la liste ComboBox
        ILayer = self.ComboBox.currentIndex()
        ZLayer = self.iface.mapCanvas().layer(ILayer)
        self.TextEdit.setText(ZLayer.htmlMetadata())
        """
        printer = QPrinter()
        printer.setPageSize(QPrinter.A4)
        printer.setOrientation(QPrinter.Landscape)
        printer.setOutputFormat(QPrinter.NativeFormat)
        printDialog = QPrintPreviewDialog(printer)
        printDialog.setWindowTitle("Imprimer la rubrique d'aide")
        printDialog.setWindowFlags(Qt.WindowMaximizeButtonHint)
        printDialog.paintRequested.connect(self.TextEdit.print_)
        printDialog.exec_()
        """    
        return      
        


