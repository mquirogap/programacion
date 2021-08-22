import sys
import os
print(sys.argv)
argumentos={}
for p in sys.argv[1:]:
    x= p.split("=")
    print(x)
    opcion=x[0] 
    valor_opcion=x[1]
    argumentos[opcion] = valor_opcion
print(argumentos)
