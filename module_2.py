__author__ = "Thomas Escrihuela"
__version__ = "1.0"

"""
    Programme réalisé pendant la formation Python pour QGIS de 3 jours.
        MODULE 2
"""


###################
#### Libraires ####
from pprint import pprint
import sys
import os

####################
#### Paramètres ####
# Exo 1
xmin, ymin, width, height = 1.0, 2.5, 10, 20

# Exo 2
msg1, msg2, msg3, msg4 = "Voici une phrase", "et une autre phrase", "et la dernière phrase", "C'est la fin"

# Exo 3
nom_fichier = "system.txt"

# Exo 4
repertoire = "C:\MOC_Q3_STAGE"
extension = ["pdf", "txt", "shp"]


###################
#### Fonctions ####
def print_resultat(chaine, fonction):
    '''Fonction pour afficher les résultats des fonctions des exos. Commune à tous les modules.'''
    print()
    print("-" * 50)
    print(chaine)
    print(fonction)
    
# Exo 3
def creer_fichier(f):
    '''Fonction de création de fichier txt contenant sys.path.'''
    file = open(f, 'w')
    [file.write(f"{line}\n") for line in sys.path]
    file.close()
    
    return f"Fichier {f} créé contenant\n{open(f).read()}"
    
# Exo 4
def listdirectory(dir, list_ext):
    '''Fonction de listing des fichiers avec des extensions particulières dans un dossier particulier.'''
    r = []
    [r.append(os.path.join(root, file)) for root, dirs, files in os.walk(dir) for file in files for ext in list_ext if file.endswith(ext)]
    
    return '\n'.join(r)
    
    
#################
#### Classes ####
# Exo 1
class Rectangle():
    '''Une classe de rectangle défini par le lowerleft et width/height'''
    def __init__(self, xmin, ymin, width, height):
        self.xmin = xmin
        self.ymin = ymin
        self.height = height
        self.width = width
    
    def get_lowerright(self):
        ''''Récupère le point bas droit'''
        return self.xmin + self.width, self.ymin
    
    def get_width(self):
        ''''Récupère la largeur'''
        return self.width

    def get_surf(self):
        ''''Récupère la surface'''
        return self.width * self.height
    
    def __repr__(self):
        '''Surcharge la fonction print() pour afficher la réponse à l'exo'''
        return f"Point bas-droit : {self.get_lowerright()}\nLargeur : {self.width} \nSurface {self.get_surf()}"

# Exo 2
class TableauNoir():
    '''Une classe de tableaunoir défini par une surface'''
    def __init__(self):
        self.surface = ''
    
    def set_surface(self, string):
        ''''Ecrit sur la surface'''
        self.surface += f"\n{string}"
    
    def del_surface(self):
        ''''Efface le message'''
        self.surface = ''
    
    def __repr__(self):
        '''Surcharge la fonction print() pour afficher la réponse à l'exo'''
        return f"--Voici le message--{self.surface}" if self.surface else "====>  ATTENTION SURFACE VIDE  <===="


###############
#### MAIN #####
###############
if __name__ == '__main__':

    print_resultat("EXO 1 : Créer une classe rectangle :", Rectangle(xmin, ymin, width, height))
    print_resultat("EXO 2 : Création de la classe TableauNoir", '')
    myTab = TableauNoir()
    myTab.set_surface(msg1)
    print(myTab)
    myTab.set_surface(msg2)
    print(myTab)
    myTab.set_surface(msg3)
    print(myTab)
    myTab.del_surface()
    print(myTab)
    myTab.set_surface(msg4)
    print(myTab)
    print_resultat("EXO 3 : Créer un fichier texte :", creer_fichier(nom_fichier))
    print_resultat("EXO 4 : Liste tous les fichiers d'extension dans un répertoire :", listdirectory(repertoire, extension))

    