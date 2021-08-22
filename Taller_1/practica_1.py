import sys
import os
import os.path

#The following function takes all the options given by the user and saves them in a dictionary
#That will later allow us to use those options as imputs in different functions

def diccionario_argumentos():
    argumentos={}
    if len(sys.argv) < 4:
        print("No está ingresando los suficientes argumentos. La sintaxis es <data> <id> <query>, en ese orden")
        return {}
    else:
        for p in sys.argv[1:]:
            opcion = p.split("=")[0] 
            valor_opcion = p.split("=")[1] 
            argumentos[opcion] = valor_opcion
        return argumentos

#Debo hacer funciones que me permitan saber qué tipo de id está buscando el usuario, para saber si debo buscar
#dentro de los archivos por accession, name o proteína

def busqueda_por_accession(id_consulta):
    p = id_consulta.split(':')
    return p[0]=='acc'
def busqueda_por_name(id_consulta):
    p = id_consulta.split(':')
    return p[0]=='name'
def busqueda_por_prot(id_consulta):
    p = id_consulta.split(':')
    return p[0]=='prot'

#Acá haré las funciones que me permitirán abrir el archivo para saber si sí contienen la información que necesito.

def accession_en_archivo(file, accession):
    with open(file.path) as hdlr:
        for line in hdlr:
            if line.startswith("ACCESSION"):
                if accession in line:
                    return True
                else:
                    for line in hdlr:
                        if line.startswith("VERSION"):
                            return False
                        else:
                            if accession in line:
                                return True
    return False

def name_en_archivo(file, name):
    with open(file.path) as hdlr:
        for line in hdlr:
            if "ORGANISM" in line:
                if name in line:
                    return True
    return False

def protein_en_archivo(file, protein_id):
    with open(file.path) as hdlr:
        for line in hdlr:
            if "/protein_id" in line and protein_id in line:
                return True
    return False

#Aquí haré funciones, que dependiendo del tipo de id que me haya pedido el usuario, me abra cada uno de los archivos
# presentes en el path dado y lea en su interior, a ver cuáles cumplen ese id dado, y me los vaya recopilando
# en una lista    

def obtener_lista_de_archivos_por_name(path, name):
    folder = os.scandir(path)
    lista=[]
    for file in folder:
        if file.name.endswith(".gbff"):
            if name_en_archivo(file, name):
                    lista.append(file.name)
    return lista


def obtener_lista_de_archivos_por_accession(path, accession):
    folder = os.scandir(path)
    lista=[]
    for file in folder:
        if file.name.endswith(".gbff"):
            if accession_en_archivo(file, accession):
                    lista.append(file.name)
    return lista

def obtener_lista_de_archivos_por_prot(path, prot):
    folder = os.scandir(path)
    lista=[]
    for file in folder:
        if file.name.endswith(".gbff"):
            if protein_en_archivo(file, prot):
                    lista.append(file.name)
    return lista


#Voy a hacer una función que me busque mi lista de archivos, ahora debo empezar a recopilar las listas de archivos que me cumplan con las condiciones que me dio el usuario

def obtener_lista_archivos(path, query_id): #aquí query_id es un parámetro
    lista_archivos=[]
    id=query_id.split(':')[1]
    if busqueda_por_accession(query_id):
        lista_archivos = obtener_lista_de_archivos_por_accession(path, id)
    elif busqueda_por_name(query_id):
        lista_archivos = obtener_lista_de_archivos_por_name(path, id)
    elif busqueda_por_prot(query_id):
        lista_archivos = obtener_lista_de_archivos_por_prot(path, id)
    else:
        print("La opción seleccionada para la consulta id, no es la correcta. Son <acc> <name> o <prot>")
    print(lista_archivos)
    return lista_archivos

#A continuación tendremos una función que me permite saber qué tipo de query me está pidiendo el usuario, para que la función
#devuelva lo pedido

def query_detallado(lista, path):
    lista_linea=[]
    folder = os.scandir(path)
    contador=0
    for file in folder:
        for x in lista:
            if file.name.endswith(".gbff") and file.name==x:
                with open(file) as file:
                    lines=file.readline()
                    lista_linea.append(lines)      
    print(lista_linea)


        
#def query_detallado(lista, path):
    #lista_linea=[]
    #for x in lista:
        #with open(x.path) as file:
            #lines=file.readline()
           # lista_linea.append(lines)
   # print(lista_linea)        


#Voy a tener una función que me sirva para abrir las funciones previas. Es el entry point.

def main():
    #recoger parámetros de línea de comandos y armar diccionario
    dic_comandos = diccionario_argumentos() #obtengo diccionario
    consulta_id = dic_comandos['id']
    id=consulta_id.split(':')[1] #esto fue un ensayis que hice para ver si sí me funcionaba separar el id así y lo imprimí por silas
    print(id)
    path = dic_comandos["data"]
    query= dic_comandos['query']
    lista=obtener_lista_archivos(path, consulta_id)
    print(query)
    obtener_lista_archivos(path, consulta_id) #esto que estoy llamando acá "consulta_id" es un argumento y cuando lo llamo 
    #al definir una función se llama parámetro.
    #lista=obtener_lista_archivos(path, consulta_id)
    query_detallado(lista,path)
    


    print(dic_comandos) #con esto logro imprimir mis comandos para probar que si funcione

main()