#Instancier les variables
prenom = "jean"
nom = "Haimar"
age = 21
ministere1 = "MTES"
ministere2 = "PCT"

MonMess = "Je m'appelle %s %s, j'ai %s ans. Sur mon badge, il est écrit : %s %s – Ministère %s / %s" %(prenom,nom, age, nom.upper(),prenom.capitalize(),ministere1, ministere2 )
print(MonMess)
