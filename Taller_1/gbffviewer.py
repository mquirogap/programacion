import sys
print(sys.argv)
import os
#Antes de empezar se definen los strings que se le pediran al usuario, para saber qué buscar

def diccionario_argumentos():
    argumentos={}
    for p in sys.argv[1:]:
        opcion = p.split("=")[0] 
        valor_opcion = p.split("=")[1] 
        argumentos[opcion] = valor_opcion
    return argumentos

print(diccionario_argumentos())

    



#a continuación se definirá una función que me permitirá obtener una lista de los nombres de unos archivos 
# contenidos en una carpeta. Se definió el parámetro ruta, de manera que el usuario pueda indicar la ubicación 
# de la carpeta que desea que sea evaluada. 

def lista_de_archivos(ruta):
    filelist=[]
    with os.scandir(ruta) as entries:
        for e in entries:
            filelist.append(e.name)
    return filelist
print(lista_de_archivos("./gbff"))








