# (c) Didier  LECLERC CPII / DON / ROUEN
# cree Fevrier 2019 
# Version pour Qgis 3.x

import qgis
from qgis.utils import qgsfunction

from qgis import *
from qgis.core import *
from qgis.gui import *

@qgsfunction(3, "JISIG 04 décembre 2013")
def MaFonction_Etiquette(values, feature, parent):
    """
       Returns les arguments
       <h4>Syntax</h4>
       <pre>$MaFonction_Etiquette</pre>

       <h4>Arguments</h4>
       Trois
       - Param 0
       - Param 1
       - Param 2
       
       <h4>Exemple</h4>
       $MaFonction_Etiquette("Ma Chaîne", 10, 100.25) &rarr;
       - Param 0 : Ma Chaîne
       - Param 1 : 10
       - Param 2 : 100.25

   """
    return ("- Param 0 : " + str(values[0]) + "\n- Param 1 : " + str(values[1]) + "\n- Param 2 : " + str(values[2]))

@qgsfunction(0, "JISIG 04 décembre 2013")
def helloDDTxx(values, feature, parent):
    """
       Retourne un message
       <h4>Syntax</h4>
       <pre>$helloDDTxx</pre>

       <h4>Arguments</h4>
       Aucun

       <h4>Exemple</h4>
       $helloDDTxx &rarr; "Coucou !"<br>
   """
    return "Coucou !"


@qgsfunction(0, "JISIG 04 décembre 2013")
def Nombre_Objet_de_la_couche(values, feature, parent):
    """
       Retourne le nombre d'objets de la couche active
       <h4>Syntax</h4>
       <pre>$Nombre_Objet_de_la_couche</pre>

       <h4>Arguments</h4>
       Aucun

       <h4>Exemple</h4>
       $Nombre_Objet_de_la_couche &rarr; 546
   """
    layer = iface.activeLayer()
    return layer.featureCount()
    

@qgsfunction(0, "Mes fonctions")
def MajColWithcentroidX(values, feature, parent):
     """
        Get coord X from centroid object
        <h4>Syntax</h4>
        <pre>$MajColWithcentroidX</pre>

        <h4>Arguments</h4>
        None

        <h4>WARNINGS !!!</h4>
        Not use for labelling !

        <h4>Example</h4>
        $centroidX &rarr; 966537.5805<br>
    """
     for feat in iface.activeLayer().getFeatures():
         if feat.id() == feature.id() : return round(float(feat.geometry().centroid().asPoint().x()), 4)



@qgsfunction(0, "Mes fonctions")
def MajColWithcentroidY(values, feature, parent):
     """
        Get coord X from centroid object
        <h4>Syntax</h4>
        <pre>$MajColWithcentroidY</pre>

        <h4>Arguments</h4>
        None

        <h4>WARNINGS !!!</h4>
        Not use for labelling !

        <h4>Example</h4>
        $centroidY &rarr; 2358415.8551<br>
    """
     for feat in iface.activeLayer().getFeatures():
         if feat.id() == feature.id() : return round(float(feat.geometry().centroid().asPoint().y()), 4)
