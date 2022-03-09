import os

def listDirectory(_path, _listExtensions):
    print("OK")

    for dirname, dirnames, filenames in os.walk(_path):
        for filename in filenames:
            for ext in _listExtensions:
                file_temp = str(os.path.join(dirname,filename))
                ext_temp = os.path.splitext(file_temp)
                # if ext == ext_temp[1][1:]:
                if "." + ext == ext_temp[1]:
                   print("Fichier : " + str(os.path.join(dirname,filename)))

path = "c:\\MOC_Q3_Formateur"
listExtensions = ["txt", "shp", "pdf"]

listDirectory(path, listExtensions)
