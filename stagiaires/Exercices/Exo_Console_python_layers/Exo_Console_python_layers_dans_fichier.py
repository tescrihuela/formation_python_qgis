ziface = qgis.utils.iface
zList = ziface.mapCanvas().layers()
myPath = "D:\\CMSIG\\3 - Formation\\Python\\Valise_Q3_2019\\Exercices\\Exo_Console_python_layers"
myNomFileHtml = "result_prog.html"
"""
MyFileOupout = open(myPath + "\\" + myNomFileHtml,'w')

for i in range(len(zList)) :
   MyVarTempo = "<b><u>"+str(zList[i].name())+"</u></b> :\n"+str(zList[i].htmlMetadata())
   MyFileOupout.write(MyVarTempo)


MyFileOupout.close()
"""
#Test slide 17 et 18
myPath = "D:\\CMSIG\\3 - Formation\\Python\\Valise_Q3_2019\\donnees"
myNomFileQgs = "test_qgis4.qgs"
myNomFile = "zone_commune_autres"
myNomFileShp = myNomFile + ".shp"
myName = "Didier Couche chargée avec code"

zLayer =  ziface.activeLayer()
#pour subsituter le activeLayer qui n'est plus actif après le chargement du projet
for i in range(len(zList)) :

   if str(zList[i].name()) == myNomFile :
      zLayer =  zList[i]
      break

qgis.utils.iface.showAttributeTable(zLayer)
#qgis.utils.iface.showLayerProperties(zLayer)
qgis.utils.iface.zoomFull()
qgis.utils.iface.zoomToPrevious()
qgis.utils.iface.mapCanvas() 
   
qgis.utils.iface.activeLayer().name()
#qgis.utils.iface.addProject(myPath + "\\" + myNomFileQgs)
#qgis.utils.iface.addRasterLayer (PathOfTheLayer, NameForTheLayer) (1)
zlayeracharger = qgis.utils.iface.addVectorLayer (myPath + "\\Couches\\" +  myNomFileShp, myName, 'ogr')
QgsProject.instance().addMapLayer(zlayeracharger)



