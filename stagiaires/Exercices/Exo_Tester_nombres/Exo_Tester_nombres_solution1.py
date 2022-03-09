#-----------------------------------------------
#FONCTION TEST SI LE CONTENU EST UN NOMBRE FLOAT   
#-----------------------------------------------    
def is_number_float(s):
    try:
        float(s)
        return True if (float(s) ==  s) and str(s).find(".")!= -1 else False
        return True
    except ValueError:
        return False

#-----------------------------------------------
#FONCTION TEST SI LE CONTENU EST UN NOMBRE INT   
#-----------------------------------------------    
def is_number_int(s):
    try:
        int(s)
        return True if int(s) ==  s else False
    except ValueError:
        return False 


print("alpha est entier : "+str(is_number_int("alpha")))
print("100.25 est entier : "+str(is_number_int(100.25)))
print("10000 est entier : "+str(is_number_int(100000)))
print("alpha est flottant : "+str(is_number_float("alpha")))
print("100.25 est flottant : "+str(is_number_float(100.25)))
print("10000 est flottant : "+str(is_number_float(100000)))
