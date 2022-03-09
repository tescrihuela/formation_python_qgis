# -*- coding: iso-8859-1 -*-

import sys
sys.path
print(sys.path)
sys.path.append('D:\\CMSIG\\1 - National')
print(sys.path)

globalSystem = sys.path
monFichier = "system.txt"

f = open(monFichier,"w")

for myDir in globalSystem :
  f.write(myDir + "\n")

f.close()


