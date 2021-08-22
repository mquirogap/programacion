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


#a continuación se definirá una función que me permitirá obtener una lista de los nombres de unos archivos 
# contenidos en una carpeta. Se definió el parámetro ruta, de manera que el usuario pueda indicar la ubicación 
# de la carpeta que desea que sea evaluada. 

def lista_de_archivos(ruta):
    filelist=[]
    with os.scandir(ruta) as entries:
        for e in entries:
            filelist.append(e.name)
    return filelist

#este es el que me está funcionando
def intento(ruta, accession):
    lista=[]
    with open(ruta, 'r') as f:
        line= f.readline()
        words=line.split()
        if words[1]== accession:
            lista.append("GCA_009733575.1_Gyman1_genomic.gbff")
        else:
            print("not")
    return lista

def intento_3(path, accession):
    lista=[]
    for file in os.walk(path):
        with open(file, 'rt') as fd:
            line= fd.readline()
            lista.append(line.split())
        return lista

def imprimir_lista(path, accession):
    lista=[]
    files= os.listdir(path)
    for f in files:
        if f.endswith('.gbff'):
            with open(f,'r') as fd:
                line= fd. readline()
                words=line.split()
                if words[1]==accession:
                    lista.append("GCA_009733575.1_Gyman1_genomic.gbff")
                else:
                    print("not")
    return lista, files




print(imprimir_lista("/Users/quiroga/Documents/Manuela_Quiroga/EAFIT/9no_semestre/Programacion/Taller_1/gbff", "ML769383"))

def intento_4(path, accession):
    lista=[]
    files= os.listdir(path)
    for f in files:
        with open(f, 'r') as fd:
            line= fd.readline()
            words=line.split()
            if words[1]== accession:
                lista.append("GCA_009733575.1_Gyman1_genomic.gbff")
            else:
                print("not")
        return lista

#print(intento_4("/Users/quiroga/Documents/Manuela_Quiroga/EAFIT/9no_semestre/Programacion/Taller_1/gbff", "ML769383"))

def buscar_accession(ruta, accession):
    filelist=[]
    filelist_accession=[]
    with os.scandir(ruta) as entries:
        for e in entries:
            filelist.append(e.name)
    for e in filelist:
        f=open(e, 'r')
        for line in f:
            if accession in line:
                filelist_accession.append(e.name)
            else:
                pass
        return filelist_accession

