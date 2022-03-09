#MaClasse Mon rectangle
class Personne:
   def __init__(self, nom, prenom):
       self.nom = nom
       self.prenom = prenom
   def presenter(self) :
       return self.nom.upper() + " " + self.prenom
 
class Etudiant(Personne):
   def __init__(self, niveau, nom, prenom):
       Personne.__init__(self, nom, prenom)
       self.niveau = niveau
   def presenter(self):
       return "Je m'appelle " + Personne.presenter(self) + ", Etude "+ self.niveau
 
#Exemple d'appelÂ :
print(Etudiant("Licence INFO", "Dupontel", "Albert").presenter())
print(Personne("Dupontel", "Albert").presenter())
print(Etudiant("Licence INFO", "Dupontel", "Albert").presenter())
