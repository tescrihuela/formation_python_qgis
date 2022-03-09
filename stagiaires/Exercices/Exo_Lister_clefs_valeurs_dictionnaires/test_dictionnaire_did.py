# -*- coding: iso-8859-1 -*-
#Mon Dictionnaire
"""
dictionnaire = {'1':'NoBrush', '2':'SolidPattern', '3':'HorPattern', '4':'VerPattern',
          '5':'BDiagPattern', '6':'FDiagPattern','7':'CrossPattern','8':'DiagCrossPattern',
          '12':'Dense1Pattern', '13':'Dense2Pattern','14':'Dense3Pattern','15':'Dense4Pattern',
          '16':'Dense5Pattern', '17':'Dense6Pattern','18':'Dense7Pattern','19':'HorPattern',
          '20':'HorPattern','21':'HorPattern', '24':'VerPattern','25':'VerPattern','26':'VerPattern','29':'BDiagPattern',
          '30':'BDiagPattern','31':'BDiagPattern', '34':'FDiagPattern','35':'FDiagPattern','36':'FDiagPattern','39':'CrossPattern','40':'CrossPattern',
          '41':'CrossPattern'
         }
"""
#Permet de trouver le module .py
#Sinon IDLE OK mais pas sous Qgis
import sys
sys.path.append('D:\\CMSIG\\3 - Formation\\Python\\Valise_Q3_2019\\Exercices\\Exo_Lister_clefs_valeurs_dictionnaires')
#Permet de trouver le module .py

import test_dictionnaire__tableau_did

#==========================
def ListeMonDic(MyDic):
    print("ListeMonDic")
    for key in MyDic.keys():
        print("Ma clef est : " + str(key) + " et la valeur est : " + MyDic[key])

ListeMonDic(test_dictionnaire__tableau_did.dictionnaire)

#==========================
def ListeMonDicTrie(MyDic):
    print("\n\nListeMonDicTrie")
    newDic  = {}
    for key in MyDic.keys():
        newDic["{:>5}".format(key)] = MyDic[key]
    
    for key in sorted(newDic.keys()):
        print("Ma clef est : " + str(key) + " et la valeur est : " + newDic[key])
        
ListeMonDicTrie(test_dictionnaire__tableau_did.dictionnaire)

