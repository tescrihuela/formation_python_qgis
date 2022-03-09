# -*- coding: iso-8859-1 -*-
#Fonction repertoires et fichiers

"""
import os
"""
import os

def listdirectorybrut(path) :
    #dirname dossiers
    #subdirname sous dossiers
    
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames: 
            print("Dossier [" + dirname +"] sous-dossier : " + subdirname)
        for filename in filenames:
            print("Fichier : " + str(os.path.join(dirname,filename)))
            print("Fichier : " + str(dirname) + "\\" + str(filename))

def listdirectory(path,MyExtension) :
    for Myext in MyExtension :
    
        for dirname, dirnames, filenames in os.walk(path):

            for filename in filenames:
                MaChaine = os.path.splitext(str(os.path.join(dirname,filename)))
                MonExt = "." + Myext.lower()
                
                if MaChaine[1].lower()== MonExt:
                    print("Fichier : " + str(os.path.join(dirname,filename)))
    
path = "C:\\py4qgis2"
MyExtension = ('txt','wor','shp','tab','odt')

#listdirectory(path,MyExtension)
listdirectorybrut(path)
