
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QAction, QMenu , QApplication, QMessageBox
from PyQt5.QtGui import QIcon

from qgis.core import *
from qgis.gui import *

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

        self.PushButton.clicked.connect(Dialog.reject)
        self.ComboBox.currentIndexChanged.connect(Dialog.GetMetaData)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        


