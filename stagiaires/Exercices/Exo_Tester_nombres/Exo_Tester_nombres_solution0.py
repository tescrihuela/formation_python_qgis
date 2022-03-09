zListe = ("alpha", 100.25, 10000)

def is_int(value):return (type(value)== int) 
def is_float(value):return (type(value)== float)         

for elt in zListe : print(str(elt)+" retourne "+str(is_int(elt)))
for elt in zListe : print(str(elt)+" retourne "+str(is_float(elt)))
