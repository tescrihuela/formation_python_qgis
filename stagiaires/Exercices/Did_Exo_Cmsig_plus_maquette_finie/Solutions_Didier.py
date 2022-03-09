MonIface = qgis.utils.iface
MesCouches = MonIface.mapCanvas().layers()

try :
   var1 = "qgis.utils.iface : " + MonIface.activeLayer().name()
   var2 = "QgisInterface : " + qgis.gui.QgisInterface.activeLayer.__name__
   MyActiveLayer = MonIface.activeLayer()
   MyActiveLayerName = MyActiveLayer.name()

except :
   var1 = ""
   var2 = ""
   MyActiveLayer = ""
   MyActiveLayerName = ""

#==================================================
def Traitement_Couches():
    MyActiveLayer = MonIface.activeLayer()
    MyActiveLayerName = MyActiveLayer.name()
    print(MyActiveLayer)
    print(MyActiveLayerName)
    MyPath = "D:\Divers_test\\zone_commune_densite.shp"
    MyName = "Didier Couche zone_commune_densite"
    MonIface.addVectorLayer(MyPath, MyName, "ogr")

    MyActiveLayer = MonIface.activeLayer()

    #Provider
    # le conteneur de format
    MyProvider = MyActiveLayer.dataProvider()

    #Nombre d'enregistrements
    print(MyProvider.featureCount())

    # les index des attributs
    MyAttributsIndex = MyProvider.attributeIndexes()
    print(MyAttributsIndex)

    #Mes attributs
    MyAttributs = MyProvider.fields()
    
    for MyAttrib in MyAttributs:
        print(str(MyAttrib.name()) + " " + str(MyAttrib.typeName()) + " " + str(MyAttrib.type()) + " " + str(MyAttrib.length()))

    #Mes valeurs
    MyAllValues = MyActiveLayer.getFeatures(QgsFeatureRequest())
    
    for MyValue in MyAllValues:
        print(str(MyValue.attributes()))
        print(MyValue.geometry())

    MYAttribIndex = 2
    
    for feat in MyActiveLayer.getFeatures():
        print(str(feat[MYAttribIndex]))
        zGeom = feat.geometry() 
        print(str(zGeom))   

    # les Geometries

    
#==================================================
def Traitement_Couches_dico():
    MyActiveLayer = MonIface.activeLayer()
    MyActiveLayerName = MyActiveLayer.name()
    print(MyActiveLayer)

    #Provider
    # le conteneur de format
    MyProvider = MyActiveLayer.dataProvider()

    #Nombre d'enregistrements
    print(MyProvider.featureCount())

    #fields
    mListAttrib = MyProvider.fields()
    print("%s == %s" %("Liste des attributs", mListAttrib))

    #Mes attributs
    r = 0
    for (mField) in mListAttrib:
        print ("%s == %s == %s" %("Champ",str(r),  str(mField.name())))
        r += 1

    #Mes attributs en liste
    mListFieldName = [ mField.name() for mField in mListAttrib ]
   
    #Mes valeurs
    MyAllValues = MyActiveLayer.getFeatures(QgsFeatureRequest())
    
    #Création d'un dictionnaire et affichage d'un champ virtuel
    for MyValue in MyAllValues:
        mMonDic = dict(zip(mListFieldName, MyValue.attributes()))
        print ("%s == %s" %("MonDic", mMonDic))
        print ("%s == %s" %("url", mMonDic["url"]))

#==================================================
def Write_File_Meta(WithStyle,encodePage):      
    myPath = "D:\\CMSIG\\3 - Formation\\Python\\Valise_Q3_2019\\Exercices\\Exo_Console_python_layers"
    myNomFileHtml = "result_prog_perso.html"

    MyFileOupout = open(myPath + "\\" + myNomFileHtml,'w')
    var3 = "Pas de selection"

    MonDebutStyle = "<html><body><meta http-equiv='Content-Type' content='text/html; charset=" + encodePage + "' />"

    if WithStyle :
       #MonDebutStyle = "<html><body><meta http-equiv='Content-Type' content='text/html; charset=" + encodePage + "' />"
       MonDebutStyle += "<font color='#0000FF' size=6 face = 'Comic sans serif'>"
       MonFinStyle = "</font></body></html>"
       Monlistview = "<style>.list-view {font-weight: bold;color: #FF0000; background-color: #cccccc;padding: 4px; border: 2px solid #FF0000}</style>" 
       Montabularview = "<style>.tabular-view {color: #547ca0; background-color: #cccccc;}</style>"
    else :
       #MonDebutStyle = ""
       MonFinStyle = ""
       Monlistview = "" 
       Montabularview = "" 

    if var1 != "" :
      print(var1)
    else :
      print(var3)
    
    if var2 != "" :
      print(var2)
    else :
      print(var3)

    for i in range(len(MesCouches)) :
       r1 = (MonDebutStyle + " Nom : " + str(MesCouches[i].name()) + MonFinStyle)
       r2 = (Monlistview + Montabularview + MesCouches[i].htmlMetadata())
       MyFileOupout.write(r1 + r2)
       
    MyFileOupout.close()          
#===                         ===
#=== Lancement des fonctions ===
WithStyle = False
WithStyle = True
encodePage = "utf-8"
encodePage = "iso-8859-1"     


#Write_File_Meta(WithStyle,encodePage)

#Lance le traitement sur les couches
#Traitement_Couches()
Traitement_Couches_dico()

