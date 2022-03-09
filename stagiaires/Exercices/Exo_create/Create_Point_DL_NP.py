# (c) Didier  LECLERC 2018
# créé mars 2018 version 3.0            

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QAction, QMenu , QApplication, QMessageBox
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import *
from PyQt5.QtGui import *

from qgis.core import *
from qgis.gui import *

import qgis

from shapely.wkb import loads
from shapely.wkt import dumps

#Ma fonction de création
def createPoints(denominateur):       
    # Création de la nouvelle couche de point et sa table attributaires
    crsDest = QSettings().value("Projections/layerDefaultCrs")
    typeAndCrsFuturLayer = "Point?crs=" + crsDest
    MyNewLayerPoint = QgsVectorLayer(typeAndCrsFuturLayer, "Creation d'une couche de point", "memory") 
    ProviderToMyNewLayerPoint = MyNewLayerPoint.dataProvider()  
    ProviderToMyNewLayerPoint.addAttributes( [ QgsField("ID", QVariant.Int),QgsField("distance", QVariant.Double),QgsField("Id_Lignes", QVariant.String , "char", 254, 0) ] )
    MyNewLayerPoint.startEditing()

    iface = qgis.utils.iface
    layer = iface.mapCanvas().currentLayer()

    counter=0
    # Boucle sur les objets sélectionnés
    for feature in layer.selectedFeatures():
        geom = feature.geometry()
        length = geom.length()

        #Juste un attribut
        MyAttribIndex1 = 1 
        MyAttribIndex2 = 0 
        My_Id_Lignes = str(feature[MyAttribIndex2]) + '_' + str(feature[MyAttribIndex1]) 

        fet = []
        delta = length/denominateur
        distance = 0

        # Boucle sur la création de possible points.
        while (distance <= length):
            myObjet = geom.asWkb().data()
            line = loads(myObjet)
            point = line.interpolate(distance)

            # Create the new feature.
            fet = QgsFeature()
            qgsgeom = QgsGeometry.fromWkt(dumps(point))
            fet.setGeometry(qgsgeom)
            fet.setAttributes([ counter, distance,My_Id_Lignes])
            ProviderToMyNewLayerPoint.addFeatures([ fet ])

            MyNewLayerPoint.updateExtents()  
            counter+=1
            distance+= delta
     
    MyNewLayerPoint.commitChanges()
    QgsProject.instance().addMapLayer(MyNewLayerPoint)

x = createPoints(5)       
