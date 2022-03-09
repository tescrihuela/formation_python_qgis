# -*- coding: UTF-8 -*-

def MyFonction(zMyChaine,tBadValue,tGoodValue) :

    for zMyValue in tBadValue :
        zMyChaine = zMyChaine.replace(zMyValue, tGoodValue)
        
    return zMyChaine

def MyFonctionPlus(zMyChaine,listBadValue,listGoodValue):
    i = 0

    while i < len(listBadValue):
        zMyChaine = zMyChaine.replace(listBadValue[i], listGoodValue[i])
        i += 1
        
    return zMyChaine
    
zText = "Voici un exemple @de ce que je souhaite realiser@<br>, pour l'exemple bien@ <br>entendu<br>."
zBadValue = ('@','<br>','#')
zGoodValue = ''

print(MyFonction(zText,zBadValue,zGoodValue))
listBadValue = ('@','<br>','#')
listGoodValue = ('', "\n","")
print(MyFonctionPlus(zText,listBadValue,listGoodValue))

