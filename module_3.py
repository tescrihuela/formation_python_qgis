import sys
sys.path.append("C:\Program Files\QGIS 3.24.0\apps\qgis\python")
import qgis
from qgis.core import *


##################
##  Paramètres  ##
# Exo 1
iface = qgis.utils.iface
l = iface.activeLayer()

#Exo 2
layers = iface.mapCanvas().layers()

# Exo 3
output_metadata_file = r"d:\Users\Administrateur\Desktop\formation_python_qgis\resultats.html"
Monlistview = "<style>.list-view {font-weight: bold;color: #FF0000; background-color: #cccccc;padding: 4px; border: 2px solid #FF0000}</style>"
Montabularview = "<style>.tabular-view {color: #547ca0; background-color: #cccccc;}</style>"


###################
#### Fonctions ####
def main():
    print_resultat(f"EXO 1 : Liste les champs de la couche active [{l.name()}]:", liste_champs_couche_active(l))
    print_resultat("EXO 2 : Liste toutes les couches du canvas et leur projection :", liste_couches_crs_canvas(layers))
    print_resultat("EXO 3 : Exporter les métadonnées de toutes les couches avec surcharge css :", export_metadata(output_metadata_file, layers))
    
def print_resultat(chaine, fonction):
    '''Fonction pour afficher les résultats des fonctions des exos. Commune à tous les modules.'''
    print()
    print("-" * 50)
    print(chaine)
    print(fonction)
    
# Exo 1
def liste_champs_couche_active(layer):
    '''Fonction de listing des champs de la couche active.'''
    return '\n'.join([l.fields().field(i).name() for i in range(len(layer.fields()))])

# Exo 2
def liste_couches_crs_canvas(layers):
    '''Fonction de listing des couches/crs du canvas.'''
    return '\n'.join([f"{layers[i].name()} / {layers[i].sourceCrs().description()}" for i in range(len(layers)) if layers[i].type() == QgsMapLayer.VectorLayer])

# Exo 3
def export_metadata(file, layers):
    '''Fonction d'export des métadonnées de toutes les couches du canvas avec css.'''
    f = open(file, 'w')
    f.write(Monlistview + Montabularview + '\n'.join([l.htmlMetadata() for l in layers]))
    f.close()
    return f"Création de [{file}] terminé !"


##################
###   MAIN   #####
##################
main()
