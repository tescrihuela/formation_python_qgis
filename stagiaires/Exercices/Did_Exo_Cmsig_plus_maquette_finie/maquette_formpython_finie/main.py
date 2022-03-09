# (c) Didier  LECLERC 2018
# créé mars 2018 version 3.0            

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QAction, QMenu , QApplication, QMessageBox
from PyQt5.QtGui import QIcon

from qgis.core import *
from qgis.gui import *

import os
from . import doDlgBox
from . import doAbout
from . import doListLayers

class MainPlugin(object):
  def __init__(self, iface):
    #référence à l'objet interface QGIS
    self.iface = iface

  def initGui(self):
    self.menu=QMenu("Maquette complète Formation Python Qgis 3")

    #déclaration des actions élémentaires
    menuIcon = getThemeIcon("exemple1.png")
    self.commande1 = QAction(QIcon(menuIcon),"Ligne de commande 1 ...",self.iface.mainWindow())
    self.commande1.setText("Ligne de commande 1 ...")
    self.commande1.setObjectName("commande1")

    menuIcon = getThemeIcon("exemple2.png")
    self.commande2 = QAction(QIcon(menuIcon),"Ligne de commande 2 ...",self.iface.mainWindow())
    self.commande2.setText("Ligne de commande 2 ...")
    self.commande2.setObjectName("commande2")

    menuIcon = getThemeIcon("exemple3.png")
    self.commande3 = QAction(QIcon(menuIcon),"Ligne de commande 3 ...",self.iface.mainWindow())
    self.commande3.setText("Ligne de commande 3 ...")
    self.commande3.setObjectName("commande3")

    menuIcon = getThemeIcon("exemple4.png")
    self.commande4 = QAction(QIcon(menuIcon),"Ligne de commande 4 ...",self.iface.mainWindow())
    self.commande4.setText("Ligne de commande 4 ...")
    self.commande4.setObjectName("commande4")

    menuIcon = getThemeIcon("exemple5.png")
    self.commande5 = QAction(QIcon(menuIcon),"Ligne de commande 5 ...",self.iface.mainWindow())
    self.commande5.setText("Ligne de commande 5 ...")
    self.commande5.setObjectName("commande5")

    menuIcon = getThemeIcon("about.png")
    self.about = QAction(QIcon(menuIcon), "A propos ...", self.iface.mainWindow())
    self.about.setText("A propos ...")

    #Construction du sous menu
    self.sousmenu=QMenu("Exemple de sous menu ...")
    self.sousmenu.addAction(self.commande2)
    self.sousmenu.addAction(self.commande3)
    self.sousmenu.addAction(self.commande4)
    
    #Construction du menu
    self.menu.addAction(self.commande1)
    self.menu.addSeparator()
    #    
    #Construction du sous menu
    self.menu.addMenu(self.sousmenu)
    #Construction du sous menu
    #
    self.menu.addSeparator()    
    self.menu.addAction(self.commande5)        
    self.menu.addSeparator()
    self.menu.addAction(self.about)

    """
    #Construction du menu
    self.menu.addAction(self.commande1)
    self.menu.addAction(self.commande2)
    self.menu.addSeparator()    
    self.menu.addAction(self.commande3)
    self.menu.addAction(self.commande4)
    self.menu.addAction(self.commande5)        
    self.menu.addSeparator()
    self.menu.addAction(self.about)
    """
    
    #Connection de la commande à l'action 
    self.commande1.triggered.connect(self.LoadDlgLayers)
    self.commande2.triggered.connect(self.MyMesscorrige)
    self.commande3.triggered.connect(self.MyMesscorrige)
    self.commande4.triggered.connect(self.MyMesscorrige)
    self.commande5.triggered.connect(self.LoadDlgBoxQt)
    self.about.triggered.connect(self.LoadDlgAbout)
    
    #Gestion du menu et de sa position
    #menuBar = self.iface.mainWindow().menuBar()
    #menuBar.addMenu(self.menu)

    #menuBar = self.iface.mainWindow().menuBar()
    #zMenu = menuBar
    #for child in menuBar.children():
    #    if child.objectName()== "mPluginMenu" :
    #       zMenu =  child
    #       break
    #zMenu.addMenu(self.menu)

    menuBar = self.iface.mainWindow().menuBar()
    actions = menuBar.actions()
    lastAction = actions [len(actions) - 5]
    menuBar.insertMenu (lastAction, self.menu)

    #=========================
    #Ajouter une barre d'outils'
    self.toolBarName = "Ma Barre outil Maquette complète Formation Python Qgis 3"
    self.toolbar = self.iface.addToolBar(self.toolBarName)
    # Pour faire une action
    self.toolbar.addAction(self.commande1)
    self.toolbar.addSeparator()
    self.toolbar.addAction(self.commande2)
    self.toolbar.addAction(self.commande3)
    self.toolbar.addAction(self.commande4)
    self.toolbar.addSeparator()
    self.toolbar.addAction(self.commande5)
    #=========================
    
  #Méthode au déchargement de l'extension
  def unload(self): pass   

  #Exemple d'appel d'une boîte de dialogue (ici : exemple d'objets Qt) 
  def LoadDlgBoxQt(self):
      d = doDlgBox.Dialog()
      d.exec_()

  def LoadDlgAbout(self):
      d = doAbout.Dialog()
      d.exec_()

  def LoadDlgLayers(self): 
      d = doListLayers.DialogListLayers()
      d.exec_()
  #=========================
  # Fonction de message
  def MyMesscorrige(self):
      Who = self.toolbar.sender().objectName()
        
      if Who =="commande1" :
         QMessageBox.information(None,"Information :", "!" + str(Who) + "! " + " Je suis un message d'information.<br><b>En format<b> HTML <br><hr>Notez la puissance <font color='#0000FF'>de feu</font>.")
      elif Who =="commande2" :
         QMessageBox.critical(None,"Avertissement :", "!" + str(Who) + "! " + " Je suis un message d'alerte.\nEn format texte classique.")      
      else :
         QMessageBox.warning(None,"Avertissement :", "!" + str(Who) + "! " + " Je suis un message d'alerte.\nEn format texte classique.")      

  #=========================

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
