# (c) Didier  LECLERC CPII / DON / ROUEN
# cree Fevrier 2019 
# Version pour Qgis 3.x

import qgis
from qgis.utils import qgsfunction

from qgis import *
from qgis.core import *
from qgis.gui import *

@qgsfunction(3, "Mes fonctions de la formation python")
def Mes_Etiquettes(values, feature, parent):
    """
       Returns les arguments
       <h4>Syntax</h4>
       <pre>$Mes_Etiquettes</pre>

       <h4>Arguments</h4>
       Trois
       - Param 0
       - Param 1
       - Param 2
       
       <h4>Exemple</h4>
       $Mes_Etiquettes("Ma Chaîne", 10, 100.25) &rarr;
       - Param 0 : Ma Chaîne
       - Param 1 : 10
       - Param 2 : 100.25

   """
    return ("- Param 0 : " + str(values[0]) + "\n- Param 1 : " + str(values[1]) + "\n- Param 2 : " + str(values[2]))

@qgsfunction(0, "Mes fonctions de la formation python")
def MessageBienvenue(values, feature, parent):
    """
       Retourne un message
       <h4>Syntax</h4>
       <pre>$MessageBienvenue</pre>

       <h4>Arguments</h4>
       Aucun

       <h4>Exemple</h4>
       *MessageBienvenue &rarr; "Coucou !, nous sommes en formation "<br>
   """
    return "Coucou !, nous sommes en formation"


@qgsfunction(0, "Mes fonctions de la formation python")
def countfeatures(values, feature, parent):
    """
       Retourne le nombre d'objets de la couche active
       <h4>Syntax</h4>
       <pre>$countfeatures</pre>

       <h4>Arguments</h4>
       Aucun

       <h4>Exemple</h4>
       $countfeatures &rarr; 546<br>
   """
    layer = iface.activeLayer()
    return layer.featureCount()
