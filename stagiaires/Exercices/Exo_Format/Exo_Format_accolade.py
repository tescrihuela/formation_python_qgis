#Instancier les variables
ministere1 = "MTES"
ministere2 = "MCT"
nom = "Haimar"
prenom = "jean"
age = 21

MonMess = "Je m'appelle {3} {2}, j’ai {4} ans."
MonMess = MonMess + " Sur mon badge, il est écrit : {5} {6} – Ministère {0} / {1}" 
MonMess = MonMess.format(ministere1, ministere2, nom, prenom, age, nom.upper(),prenom.capitalize())
print(MonMess)
