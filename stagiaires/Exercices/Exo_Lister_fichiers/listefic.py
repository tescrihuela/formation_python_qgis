import sys
file_path = "c:\\MOC_Q3_FORMATEUR\\system.txt"
liste_folder = sys.path
liste_folder.append("c:\\MOC_Q3_FORMATEUR")
with open(file_path, 'w') as f:
    for folder in liste_folder:
        f.write(str(folder) + "\n")
