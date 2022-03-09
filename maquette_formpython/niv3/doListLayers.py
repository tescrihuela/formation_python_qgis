from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *          
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QMessageBox

from qgis.core import *

from .listlayers import Ui_Dialog

class DialogListLayers(QDialog, Ui_Dialog):
      def __init__(self):
            QDialog.__init__(self)
            self.setupUi(self)

      def reject(self):
          if QMessageBox.question(None, "Confirmation", "Je suis une demande de confirmation.\nConfirmez-vous la fermeture de la boîte de dialogue ?",QMessageBox.Yes|QMessageBox.No) ==  QMessageBox.Yes : self.hide()
          else : self.show()
