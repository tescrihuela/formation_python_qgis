__author__ = "Thomas Escrihuela"
__version__ = "1.0"

"""
    Programme réalisé pendant la formation Python pour QGIS de 3 jours.
        MODULE 1
"""


###################
#### Libraires ####
from pprint import pprint


####################
#### Paramètres ####
# Exo 1
ministere = "mtes"
organisme_initial = "ign"
organisme_actuel = "cerema"
nom = "escrihuela"
prenom = "thomas"
age = "33"

# Exo 2
phrase = "Ceci est une phrase avec @ et <br> et autre chose"
char_to_delete = {
    '@': '',
    '<br>': '\n'
}

# Exo 3
tBrush = {
    "ok": "test",
    "toto": "okzaoekzaeoz",
    1: 1000,
    "temp": ["ok", "okolkokok"]
}


###################
#### Fonctions ####
def print_resultat(chaine, fonction):
    '''Fonction pour afficher les résultats des fonctions des exos'''
    print()
    print("-" * 50)
    print(chaine)
    print(fonction)

def presente_toi(min, org_i, org_a, nom, prenom, age):
    message = "\n"
    message += "Bonjour je m'appelle {} {}.\n"
    message += "J'ai {} ans.\n"
    message += "Au début, j'étais à {} et aujourd'hui je suis à {}.\n"
    message += "Dans tous les cas, j'ai passé ma vie au {}.\n"
    full_message = message.format(prenom.capitalize().center(10), nom.capitalize().center(10), age, organisme_initial.upper(), organisme_actuel.upper(), ministere.upper())
    
    return full_message

def nettoie(chaine, liste_caracteres):
    '''Exo 2'''
    for char in liste_caracteres:
        chaine = chaine.replace(char, char_to_delete[char])

    return chaine

def printDicTrie(my_dict):
    '''Exo 3'''
    dict_sorted = dict(sorted(my_dict.items(), key=lambda x: str(x[1]))) # dict sorted by value
    for k, v in dict_sorted.items():
        print(f"Ma clef est : {str(k)} et la valeur est : {str(v)}")     # utilisation de fstring

def squared(n):    
    '''Exo 4'''
    r = [x**2 for x in range(n)]
    return r


###############
#### MAIN #####
###############
if __name__ == '__main__':

    print_resultat("EXO 1 : Se présenter avec un formattage de string :", presente_toi(ministere, organisme_initial, organisme_actuel, nom, prenom, age))
    print_resultat("EXO 2 : Suppression des caractères spéciaux :", nettoie(phrase, char_to_delete))
    print_resultat("EXO 3 : Affichage de dictionnaire trié selon la valeur :", printDicTrie(tBrush))
    print_resultat("EXO 4 : Créer la liste des carrés des 10 premiers entiers :", squared(10))

    
    