from PyQt5.QtCore import *          
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog

from qgis.core import *
from .dlgBox import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
    
		
