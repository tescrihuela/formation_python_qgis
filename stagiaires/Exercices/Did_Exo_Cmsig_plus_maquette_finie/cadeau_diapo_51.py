def Traitement_Couches():
    MyActiveLayer = qgis.utils.iface.activeLayer()
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
          print(str(MyAttrib.name()) + " " + str(MyAttrib.typeName()) + " " +
          str(MyAttrib.type())            + " " + str(MyAttrib.length()))

    #Mes valeurs
    MyAllValues = MyActiveLayer.getFeatures(QgsFeatureRequest())
    
    for MyValue in MyAllValues:
        print(str(MyValue.attributes()))
        print(MyValue.geometry())

#Lance le traitement sur les couches
Traitement_Couches()