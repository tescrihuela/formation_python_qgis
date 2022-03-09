import os
#-----------------------------------------------
#FONCTION DE RECHERCHE DE FICHIERS OS.WALK
#-----------------------------------------------

def listdirectory(path):
    if os.path.exists(path):
        for dirname, dirnames, filenames in os.walk(path):
            for subdirname in dirnames: print(">> Analyse du dossier [" + dirname +"] sous-répertoire : " + subdirname)
            for filename in filenames:
                #scandirectory(os.path.join(dirname, filename))
                scan(os.path.join(dirname, filename))
    else: print("Le dossier "+str(path)+" est inconnu.")            

def scan(currentFile):
    #Exemple de filtres multiples ....
    #zFilter = "mif|jpg|tab|"
    zFilter = ".tab|"
    if os.path.exists(currentFile):
        if os.path.isfile(currentFile):
            textension = currentFile[currentFile.rfind("."):].lower()
            if zFilter.find(textension+"|")!=-1:
                print("B" + str(textension))
                print("                 Fichier : "+str(currentFile))
    return 
"""
def scandirectory(currentFile):
    #Exemple de filtres multiples ....
    #zFilter = "mif|jpg|tab|"
    zFilter = ".tab|"
    if os.path.exists(currentFile):
        if os.path.isfile(currentFile):
            textension = os.path.splitext(currentFile)
            extension = textension[len(textension)-1].lower()
            print("B" + str(textension))
            if zFilter.find(extension+"|")!=-1 and extension!="":
                print("                 Fichier : "+str(currentFile))
    return 
"""
listdirectory("C:\\py4qgis2")

