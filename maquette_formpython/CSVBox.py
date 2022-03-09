import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QAction, QMenu , QApplication, QMessageBox, QDialog, QFormLayout, QPushButton
from PyQt5.QtGui import QIcon

from qgis.core import *
from qgis.gui import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.new_dialog = QDialog()
        self.new_dialog.resize(630, 150)
        
        self.map_layer_combo_box = QgsMapLayerComboBox()
        self.map_layer_combo_box.setCurrentIndex(0)
        self.map_layer_combo_box.setFilters(QgsMapLayerProxyModel.VectorLayer)   # Filtre et ne sort que les layer vector
        
        self.ok_button = QPushButton("Exporter en csv")
        self.ok_button.setGeometry(QtCore.QRect(200, 150, 100, 40))
        # self.ok_button.resize(20, 20)
        self.ok_button.clicked.connect(self.export_csv)
        
        
        self.layout = QFormLayout()
        self.layout.addWidget(self.map_layer_combo_box)
        self.layout.addWidget(self.ok_button)

        self.new_dialog.setWindowTitle("Export en csv")

        self.new_dialog.setLayout(self.layout)
        self.new_dialog.exec_()
        
        
    def export_csv(self):
        layer = self.map_layer_combo_box.currentLayer()
        csv = r"d:\Users\Administrateur\Desktop\formation_python_qgis\table.csv"
    
        fieldnames = [field.name() for field in layer.fields()]
        features = layer.getFeatures()

        with open(csv, 'w') as output_file:
            line = ','.join(name for name in fieldnames) + '\n'
            output_file.write(line)
            for current, f in enumerate(features):
                line = ','.join(str(f[name]) for name in fieldnames) + '\n'
                output_file.write(line)

        msg = QMessageBox.information(None, "Succès de l'export", f"Vous avez bien exporté <font color='#FF0000'><b>{self.map_layer_combo_box.currentLayer().name()}</b></font> dans<br>Chemin : <a href={csv}>{csv}</a>")
        
        