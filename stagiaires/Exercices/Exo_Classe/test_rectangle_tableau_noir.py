class TableauNoir: 
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
    est 'surface'"""

    def __init__(self):
        """Par défaut, notre surface est vide"""
        self.surface = ""

    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""

        if self.surface != "":
           self.surface += "\n"
        self.surface += message_a_ecrire

    def lire(self):
        """Cette méthode se charge d'afficher, grâce à print,
        la surface du tableau"""
        print(self.surface)

    def effacer(self):
        """Cette méthode permet d'effacer la surface du tableau"""
        self.surface = ""

tab = TableauNoir()
monMess = "Coucou, comment vous sentez-vous à ce moment de la formation ?"
tab.ecrire(monMess)
print("\npremière lecture")
tab.lire()
monMess = "J'attends pas forcément de réponse"
tab.ecrire(monMess)
print("\nseconde lecture")
tab.lire()
tab.effacer()
print("\nMessage effacé")
print( "le message est effacé" if tab.effacer() == None else str(tab.effacer()))
