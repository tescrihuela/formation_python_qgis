import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QAction, QMenu , QApplication, QMessageBox, QDialog, QFormLayout, QPushButton, QComboBox, QDoubleSpinBox
from PyQt5.QtGui import QIcon

from qgis.core import *
from qgis.gui import *

from urllib.request import urlopen, HTTPError
import ssl
import xml.etree.ElementTree as ET

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.new_dialog = QDialog()
        self.new_dialog.resize(630, 150)
        
        self.map_layer_combo_box = QgsMapLayerComboBox()
        self.map_layer_combo_box.setCurrentIndex(0)
        self.map_layer_combo_box.setFilters(QgsMapLayerProxyModel.PointLayer)   # Filtre et ne sort que les layer vector
        
        graphe = ("Pieton","Voiture")
        self.comboBox = QComboBox()
        self.comboBox.setGeometry(QtCore.QRect(90,25,150,23))
        self.comboBox.setObjectName("comboBox")
        #Exemple d'alimentation de la QComboBox avec LstOPGEO
        for i in graphe:  self.comboBox.addItem(i)
        
        self.doubleSpinBox = QDoubleSpinBox()
        self.doubleSpinBox.setGeometry(QtCore.QRect(380,25,60,25))
        self.doubleSpinBox.setMaximum(60000)
        self.doubleSpinBox.setMinimum(0)
        self.doubleSpinBox.setValue(600)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        
        self.ok_button = QPushButton("Lancer le calcul d'isochrones")
        self.ok_button.setGeometry(QtCore.QRect(200, 150, 100, 40))
        # self.ok_button.resize(20, 20)
        self.ok_button.clicked.connect(self.compute_isochrone)
        
        
        self.layout = QFormLayout()
        self.layout.addWidget(self.map_layer_combo_box)
        self.layout.addWidget(self.comboBox)
        self.layout.addWidget(self.doubleSpinBox)
        self.layout.addWidget(self.ok_button)

        self.new_dialog.setWindowTitle("Calculer des isochrones depuis le Géoportail")

        self.new_dialog.setLayout(self.layout)
        self.new_dialog.exec_()
        
        
    def compute_isochrone(self):
        layer = self.map_layer_combo_box.currentLayer()
        features = layer.getFeatures()
        new_layer = QgsVectorLayer("polygon?crs=epsg:2154", "Isochrones", "memory")
        for field in layer.fields():
            new_layer.dataProvider().addAttributes([field])
        new_layer.updateFields()
        new_layer.startEditing()

        temps = int(self.doubleSpinBox.value())
        # temps = 600
        graphe = self.comboBox.currentText()
        
        print(temps)
        print(graphe)

        for current, feature in enumerate(features):
            geom = feature.geometry()
            if not geom:
                QMessageBox.warning(None, "Attention", f"[WARN] L'entité d'id {feature.id()} n'a pas de géométrie associée")
                continue
            
            coordX = geom.asPoint().x()
            coordY = geom.asPoint().y()
            xy = str(coordX) + "," + str(coordY)            
            
            req = f"https://wxs.ign.fr/choisirgeoportail/isochrone/isochrone.xml?location={xy}&method=time&graphName={graphe}&exclusions=&time={temps}&holes=false&smoothing=true&srs={layer.sourceCrs().authid()}"
            context = ssl._create_unverified_context()
            
            c = 0
            ok = False
            while (not ok) and (c < 5):
                c+=1
                try:
                    response = urlopen(req,context=context).read()
                    ok = True
                except HTTPError as e:
                    # feedback.pushInfo("Erreur : " + e.reason + ". Essai " + str(c) + "...")
                    pass

            root = ET.fromstring(response)
            isochrone_geom = root.find('wktGeometry').text
            print(isochrone_geom)
            
            feat = QgsFeature(feature)
            feat.setGeometry(QgsGeometry.fromWkt(isochrone_geom))

            new_layer.addFeature(feat)
            
        new_layer.commitChanges()
        # new_layer.updateExtents()

        print(f"Nombre de feature : {new_layer.featureCount()}")
        
        QgsProject.instance().addMapLayer(new_layer)