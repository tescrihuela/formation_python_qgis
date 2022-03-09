# -*- coding: iso-8859-1 -*-

def NetStrInfos(nStr, ListCarac):
    for i in range(len(ListCarac)): nStr = nStr.replace(ListCarac[i], "")
    return nStr

nStr = "Voici un exemple @de ce que je souhaite réaliser@<br>, pour l'exemple bien@ <br>entendu<br>."
print(NetStrInfos(nStr, ("@", "<br>")))
