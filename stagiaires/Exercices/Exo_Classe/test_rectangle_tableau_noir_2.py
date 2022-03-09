

class TABLEAUNOIR() :
    def __init__(self) :
        self.monMess = ""  # Initialisation de mon attribut message
        return

    def ecrire(self,_mess) :
        if self.monMess != "" :
           self.monMess += "\n"  
        self.monMess += str(_mess)
        return

    def afficher(self) :
        if self.monMess != "" :
           print(self.monMess)
        return

    def effacer(self) :
        self.monMess = ""
        print("je viens d'éffacer mon message")
        return

monTableauNoir = TABLEAUNOIR()

zMess = "Couoou, on commence à fatiguer !!"
monTableauNoir.ecrire(zMess)
monTableauNoir.afficher()


zMess = "c'est bientôt fini."
monTableauNoir.ecrire(zMess)
monTableauNoir.afficher()
monTableauNoir.effacer()
monTableauNoir.afficher()

    
