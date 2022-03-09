import os
import glob
#-----------------------------------------------
#FONCTION DE RECHERCHE DE FICHIERS GLOB.GLOB
#-----------------------------------------------
def listdirectory(path):
    zPath = os.path.join(path, '*')
    for currentFile in glob.glob(zPath):
        if os.path.isdir(currentFile):
           print(">> Analyse du dossier : " + currentFile)
           listdirectory(currentFile)
        else : scandirectory(currentFile)
    return 


def scandirectory(currentFile):
    #Exemple de filtres multiples ....
    #zFilter = "mif|jpg|tab|"
    zFilter = ".wor|.tab|.shp|.mif|"
    if os.path.exists(currentFile):
        if os.path.isfile(currentFile):
            textension = os.path.splitext(currentFile)
            extension = textension[len(textension)-1].lower()
            if zFilter.find(extension+"|")!=-1 and extension!="": print("                 Fichier : "+str(currentFile))
    return 


listdirectory("C:\\")
