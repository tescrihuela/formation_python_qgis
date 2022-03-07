# Notes intéressantes


## Égalité et référence des objets 

```

str_list = ['Pommes', 'Poires', 'Cerises', 'Fraises', 'Patates', 'Avocats']
str_list2 = str_list
str_list.append(‘Prunes’)

## Dans ce cas, les deux listes pointent sur le même objet ! => str_list est modifiée, str_list2 supporte la même modification.

#pour comparer le contenu de 2 listes
print(str_list == str_list2) # True
#pour comparer la référence de 2 listes
print(str_list is str_list2) # True



str_list = ['Pommes', 'Poires', 'Cerises', 'Fraises', 'Patates', 'Avocats']
str_list2 = list(str_list)

## Dans ce cas, les deux listes ne pointent pas sur le même objet ! On récupère le contenu de la liste !

#pour comparer le contenu de 2 listes
print(str_list == str_list2) # True
print(str_list is str_list2) # False
str_list.append(‘Prunes’)
#pour comparer le contenu de 2 listes
print(str_list == str_list2) # False
#pour comparer la référence de 2 listes
print(str_list is str_list2) # False

```

## Gestion des modules

| Opération | Interprétation |  
| --- | --- |  
| from .module import nom | Récupère un nom (classe) particulière dans un module |  
| from .module import * | Récupère tous les noms à la racine d'un module |  
| from . import module | Récupère tous les noms à la racine d'un module / Appel d’une fonction en précisant le nom du module |  
| import module | Récupère un module dans son intégralité |  
