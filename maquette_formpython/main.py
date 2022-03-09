# (c) Didier  LECLERC 2018
# créé mars 2018 version 3.0            

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import qgis
from PyQt5.QtWidgets import QAction, QMenu , QApplication, QMessageBox, QDialog, QFormLayout, QPushButton
from PyQt5.QtGui import QIcon

from qgis.core import *
from qgis.gui import *

import os
from . import doDlgBox, doCSVBox, doIsochroneBox, doListLayers, doAbout

class MainPlugin(object):
  def __init__(self, iface):
    #référence à l'objet interface QGIS
    self.iface = iface

  def initGui(self):
    self.menu=QMenu("Mon propre plugin")

    menuIcon = getThemeIcon("exemple2.png")
    self.commande2 = QAction(QIcon(menuIcon),"Calcule une couche isochrone",self.iface.mainWindow())
    self.commande2.setText("Calcule une couche isochrone")
    
    menuIcon = getThemeIcon("exemple3.png")
    self.commande3 = QAction(QIcon(menuIcon),"Exporte la table attributaire d'un layer en csv",self.iface.mainWindow())
    self.commande3.setText("Exporte la table attributaire d'un layer en csv")

    menuIcon = getThemeIcon("exemple4.png")
    self.commande4 = QAction(QIcon(menuIcon),"Quelle est la couche active ?",self.iface.mainWindow())
    self.commande4.setText("Quelle est la couche active ?")

    menuIcon = getThemeIcon("exemple5.png")
    self.commande5 = QAction(QIcon(menuIcon),"Métadonnées",self.iface.mainWindow())
    self.commande5.setText("Métadonnées")
    
    menuIcon = getThemeIcon("exemple5.png")
    self.commande6 = QAction(QIcon(menuIcon),"Cette action est incroyable",self.iface.mainWindow())
    self.commande6.setText("Cette action est incroyable")

    menuIcon = getThemeIcon("about.png")
    self.about = QAction(QIcon(menuIcon), "A propos ...", self.iface.mainWindow())
    self.about.setText("A propos ...")

    #Construction du menu
    self.myMenu = QMenu("Menu de Thomas")
    self.myMenu.addAction(self.commande2)
    self.myMenu.addAction(self.commande3)
    self.myMenu.addAction(self.commande4)
    self.myMenu.addAction(self.commande5)
    self.myMenu.addAction(self.commande6)
    self.menu.addMenu(self.myMenu)
    self.menu.addSeparator()
    self.menu.addAction(self.about)
    
    #Connection de la commande à l'action 
    self.commande2.triggered.connect(self.LoadIsochroneBox)
    self.commande3.triggered.connect(self.LoadCSVBox)
    self.commande4.triggered.connect(self.print_active_layer)
    self.commande5.triggered.connect(self.LoadListLayers)
    self.commande6.triggered.connect(self.LoadDlgBoxQt)
    self.about.triggered.connect(self.LoadAbout)
    
    
    #############################
    ###  Positionnement du plugin
    
    ## Ajouter le plugin en tant que menu à la fin de la barre
    # menuBar = self.iface.mainWindow().menuBar()
    # menuBar.addMenu(self.menu)
    
    ## Ajouter le plugin en tant que menu en position z-5
    # menuBar = self.iface.mainWindow().menuBar()
    # actions = menuBar.actions()
    # lastAction = actions[len(actions) - 5]
    # menuBar.insertMenu(lastAction, self.menu)
    
    ## Ajouter le plugin au menu "Extensions"
    menuBar = self.iface.mainWindow().menuBar()
    zMenu = menuBar
    for child in menuBar.children():
      if child.objectName()== "mPluginMenu" :
        zMenu = child
        break
    zMenu.addMenu(self.menu)
    
    self.toolBarName = "Barre de ouf !"
    self.toolbar = self.iface.addToolBar(self.toolBarName)
    self.toolbar.addAction(self.commande3)
    self.toolbar.addAction(self.commande4)
    self.toolbar.addAction(self.commande5)
    
    ###  Fin Positionnement du plugin
    #################################


  #Méthode au déchargement de l'extension
  def unload(self): pass   

  #Exemple d'appel d'une boîte de dialogue (ici : exemple d'objets Qt) 
  def LoadDlgBoxQt(self):
    d = doDlgBox.Dialog()
    d.exec_()
    
  #Exemple d'appel d'une boîte de dialogue (ici : exemple d'objets Qt) 
  def LoadAbout(self):
    d = doAbout.Dialog()
    d.exec_()
    
  def LoadListLayers(self):
    d = doListLayers.DialogListLayers()
    d.exec_()
      
  #Exemple d'appel d'une boîte de dialogue (ici : exemple d'objets Qt) 
  def LoadCSVBox(self):
    '''Boite de dialogue pour exporter la table attributaire d'une couche en csv'''
    d = doCSVBox.Dialog()
  
  #Exemple d'appel d'une boîte de dialogue (ici : exemple d'objets Qt) 
  def LoadIsochroneBox(self):
    '''Boite de dialogue pour créer une couche d'isochrone'''
    d = doIsochroneBox.Dialog()
    
  def print_active_layer(self):
    '''Affiche le layer actif'''
    l = qgis.utils.iface.activeLayer()
    if l:
      msg = QMessageBox.information(None, "Information", f"Couche active : {l.name()} ")
    else:
      msg = QMessageBox.warning(None, "Avertissement", "Aucune Couche sélectionnée !")
  






#Fonction de reconstruction du chemin absolu vers la ressource image
def getThemeIcon(theName):
    myPath = CorrigePath(os.path.dirname(__file__));
    myDefPathIcons = myPath + "/icons/"
    myDefPath = myPath.replace("\\","/")+ theName;
    myDefPathIcons = myDefPathIcons.replace("\\","/")+ theName;
    myCurThemePath = QgsApplication.activeThemePath() + "/plugins/" + theName;
    myDefThemePath = QgsApplication.defaultThemePath() + "/plugins/" + theName;
    #Attention, ci-dessous, le chemin est à persoonaliser :
    #remplacer "extension" par le nom du répertoire de l'extension.
    myQrcPath = "python/plugins/extension/" + theName;
    if QFile.exists(myDefPath): return myDefPath
    elif QFile.exists(myDefPathIcons): return myDefPathIcons  
    elif QFile.exists(myCurThemePath): return myCurThemePath
    elif QFile.exists(myDefThemePath): return myDefThemePath
    elif QFile.exists(myQrcPath): return myQrcPath
    elif QFile.exists(theName): return theName
    else: return ""

#Fonction de correction des chemins
#(ajout de slash en fin de chaîne)
def CorrigePath(nPath):
    nPath = str(nPath)
    a = len(nPath)
    subC = "/"
    b = nPath.rfind(subC, 0, a)
    if a != b : return (nPath + "/")
    else: return nPath  
