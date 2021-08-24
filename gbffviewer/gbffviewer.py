import sys
import os
import os.path

#Función diccionario, permite al usuario guardar las opciones de búsqueda del usuario

def diccionario_argumentos():
    argumentos={}
    if len(sys.argv) < 4:
        print("No está ingresando los suficientes argumentos. La sintaxis es <data> <id> <query>, en ese orden y si query=proteinseq debe adicionar <protein_seq>")
        return {}
    else:
        for p in sys.argv[1:]:
            opcion = p.split("=")[0] 
            valor_opcion = p.split("=")[1] 
            argumentos[opcion] = valor_opcion
        return argumentos

#Función obtener lista de archivos, permite recopilar los archivos que me cumplan con las condiciones que me dio el usuario

def obtener_lista_archivos(path, query_id): 
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
    return lista_archivos

#Funciones tipo de búsqueda ID, permiten saber qué tipo de id está buscando el usuario, para saber si debo buscar
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

#Funciones obtener lista de archivos según ID, dependiendo del tipo de id que me haya pedido el usuario, abrirá cada uno de los archivos
#presentes en el path dado y leerá su interior, viendo cuáles cumplen ese id dado, guardándolos en una lista    

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

#Funciones ID en archivo, permiten abrir el archivo para saber si sí contienen la información que necesito.

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

#Funcion para determinar que tipo de query está pidiendo el usuario            

def query_detallado(lista,path, query_id,prot_id): 
    lista_query=[]
    if query_id=="files":
        lista_query = query_files(lista, path)
        return lista_query
    elif query_id=="totals":
        lista_query = query_totals(lista,path)
        return lista_query
    elif query_id=="header":
        lista_query = query_header(lista,path)
        return lista_query
    elif query_id=="dnaseq":
        lista_query = query_dnaseq(lista,path)
        return lista_query
    elif query_id=="proteinlist":
        lista_query = query_proteinlist(lista,path)
        return lista_query
    elif query_id=="proteinseq":
        lista_query = query_proteinseq(lista,path,prot_id)
        return lista_query
    else:
        print("La opción seleccionada para la consulta query, no es la correcta. Son <files> <totals> <header> <dnaseq> <proteinlist> <proteinseq>")



#Funciones según el query pedido por el usuario, permiten abrir los archivos según el ID entregado y buscar el tipo de query que desea el usuario
#para imprimirlo.

def query_files(lista, path):
    lista_files=[]
    folder = os.scandir(path)
    for file in folder:
        for x in lista:
            if file.name.endswith(".gbff") and file.name==x:
                with open(file) as file:
                    u=x+':'+'\n'
                    lines=file.readline()
                    lista_files.append(u + lines)      
    print('\n'.join(map(str,lista_files)))

def query_totals(lista,path):
    lista_totals=[]
    folder = os.scandir(path)
    for file in folder:
        for x in lista:
            if file.name.endswith(".gbff") and file.name==x:
                with open(file) as file:
                    u=x+':'+'\n'
                    lines=file.readline()
                    lista_totals.append(u+lines) 
                    for line in file:
                        if "##Genome-Assembly-Data-START##" in line:
                            break
                    for line in file:
                        if "##Genome-Assembly-Data-END##" in line:
                            break
                        lista_totals.append(line)
    print('\n'.join(map(str,lista_totals)))

def query_header(lista,path):
    lista_header=[]
    folder = os.scandir(path)
    for file in folder:
        for x in lista:
            if file.name.endswith(".gbff") and file.name==x:
                with open(file) as file:
                    u=x+':'+'\n'
                    lines=file.readline()
                    lista_header.append(u+lines)
                    for line in file:
                        if "REFERENCE" in line:
                            break
                        lista_header.append(line)
    print('\n'.join(map(str,lista_header)))
                    
def query_dnaseq(lista,path):
    lista_dnaseq=[]
    folder = os.scandir(path)
    for file in folder:
        for x in lista:
            if file.name.endswith(".gbff") and file.name==x:
                with open(file) as file:
                    u='\n'+x+':'+'\n'
                    lines=file.readline()+'\n'
                    lista_dnaseq.append(u+lines)
                    for line in file:
                        if "ORIGIN" in line:
                            break
                    for line in file:
                        if "//" in line:
                            break
                        lista_dnaseq.append(line)
    print(''.join(map(str,lista_dnaseq)))

def query_proteinlist(lista,path):
    lista_protein=[]
    folder = os.scandir(path)
    for file in folder:
        for x in lista:
            if file.name.endswith(".gbff") and file.name==x:
                with open(file) as file:
                    u='\n'+x+':'+'\n'
                    lines=file.readline()+'\n'
                    lista_protein.append(u+lines)
                    for line in file:
                        if "CDS" in line:
                            break
                    for line in file:
                        if "/product" in line:
                            p=" "+line.split("=")[1][1:-2]
                        elif "/protein_id" in line:
                            lista_protein.append(line.split("=")[1][1:-2] + p +'\n')
    print(' '.join(map(str,lista_protein)))
                    
def query_proteinseq(lista,path,prot_id):
    lista_proteinseq=[]
    folder = os.scandir(path)
    for file in folder:
        for x in lista:
            if file.name.endswith(".gbff") and file.name==x:
                with open(file) as file:
                    u='\n'+x+':'+'\n'
                    lines=file.readline()+'\n'
                    lista_proteinseq.append(u+lines)
                    for line in file:
                        if prot_id in line:
                            break
                    for line in file:
                        if "/db_xref" in line:
                            break
                    for line in file:
                        if "/db_xref" in line:
                            continue
                        elif "/translation" in line:
                            lista_proteinseq.append(line.split("=")[1][1:])
                            break
                    for line in file:
                        if "gene" in line:
                            break
                        lista_proteinseq.append(line.lstrip(' ').replace('"', ''))         
    print(' '.join(map(str,lista_proteinseq)))


#Función principal

def main():
    dic_comandos = diccionario_argumentos() #obtengo diccionario
    consulta_id = dic_comandos['id']
    path = dic_comandos["data"]
    query_= dic_comandos['query']
    lista=obtener_lista_archivos(path, consulta_id)
    if len(sys.argv) > 4 and query_=="proteinseq": #esta funcion permite guardar la secuencia de la proteina si el query proteinseq es dado
        prot_id=dic_comandos['protein_seq']
    else:
        prot_id=None
    query_detallado(lista,path,query_, prot_id)
main()

#Opciones de comandos parar correr el programa:
#Obtener secuencia ADN de un accession: python practica_1.py data=./gbff id=acc:JADNRW010000001 query=dnaseq
#Obtener archivosque tienen un accession: python practica_1.py data=./gbff id=acc:JADNRW010000001 query=files
#Obtener Genome Assembly Data de un accession: python practica_1.py data=./gbff id=acc:JADNRW010000001 query=totals
#Obtener header de un accession: python practica_1.py data=./gbff id=acc:JADNRW010000001 query=header
#Obtener lista de proteínas de un accession: python practica_1.py data=./gbff id=acc:JADNRW010000001 query=proteinlist
#Obtener secuencia de una proteína en un accession: python practica_1.py data=./gbff id=acc:JADNRW010000001 query=proteinseq protein_seq=KAF90148
#NOTA: para las opciones de query: dnaseq y proteinlist es recomendable adicionar un archivo de salida para poder ver mejor los resultados ( >output.txt)
#python practica_1.py data=./gbff id=acc:JADNRW010000001 query=proteinlist >output.txt
