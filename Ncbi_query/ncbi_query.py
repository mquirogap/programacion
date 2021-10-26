import sys
from typing import MutableMapping
import Bio
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Entrez
from Bio.SeqRecord import SeqRecord
import pandas as pd

def diccionario_argumentos(): #Diccionario que permitirá guardar las opciones de búsqueda del usuario
    argumentos={}
    if len(sys.argv) < 3:
        print("No está ingresando los suficientes argumentos. La sintaxis es <mail> <query>, en ese orden")
        return {}
    else:
        for p in sys.argv[1:]:
            opcion = p.split("=")[0] 
            valor_opcion = p.split("=")[1] 
            argumentos[opcion] = valor_opcion
        return argumentos

def query_organism(mail, query): #Función query que permite guardar los records del NCBI que cumplen con el query realizao por el usuario
    Entrez.email=mail
    handleSearch = Entrez.esearch(db = "Nucleotide", retmax="20", term=query) #Aquí el remax puede ser editado, para que el usuario pueda obtener el número de registros deseados. En este caso se obtendrían 20
    rec=Entrez.read(handleSearch)
    return rec

def fetch_organism(idlist): #Según el id list en los registros recuperados se obtendrá la información a continuación de cada uno de los ID
    locus=[]
    strand=[]
    moltype=[]
    topology=[]
    division=[]
    source=[]
    organism=[]
    taxonomy=[]
    sequence=[]
    total_a_nuc=[]
    total_g_nuc=[]
    total_c_nuc=[]
    total_t_nuc=[]
    id_record=[]
    translation=[]
    for i in idlist:
        with Entrez.efetch(db="nucleotide", rettype="gb", id=i, retmode="txt") as handle:
            record= SeqIO.read(handle, "genbank")
            id_record.append(i)
            moltype.append(record.annotations['molecule_type'])
            topology.append(record.annotations['topology'])
            division.append(record.annotations['data_file_division'])
            source.append(record.annotations['source'])
            organism.append(record.annotations['organism'])
            taxonomy.append(record.annotations['taxonomy'])
            sequence.append(record.seq)
            total_a_nuc.append(record.seq.count("A"))
            total_g_nuc.append(record.seq.count("G"))
            total_c_nuc.append(record.seq.count("C"))
            total_t_nuc.append(record.seq.count("T"))
            locus.append(str(record.features[1].location).split('(')[0])
            strand.append(str(record.features[1].location).split('(')[1][:-1])
            translation.append(record.seq.translate())
    return moltype, topology, division, source, organism, taxonomy, sequence, total_a_nuc, total_c_nuc, total_g_nuc, total_t_nuc, locus, strand, id_record, translation
 

def pandas_cvs(id_record, moltype, locus, strand, topology, division, source, organism, taxonomy, sequence, total_a_nuc, total_g_nuc, total_c_nuc, total_t_nuc, translation):
    myDataDictionary={}
    myDataDictionary['Record']=id_record 
    myDataDictionary['Molecule_type']=moltype
    myDataDictionary['Locus']=locus
    myDataDictionary['Strand']=strand
    myDataDictionary['Topology']=topology
    myDataDictionary['Division'] = division
    myDataDictionary['Source']=source
    myDataDictionary['Organism']=organism
    myDataDictionary['Taxonomy']=taxonomy
    myDataDictionary['Sequence']=sequence
    myDataDictionary['Total_A']=total_a_nuc
    myDataDictionary['Total_G']=total_g_nuc
    myDataDictionary['Total_C']=total_c_nuc
    myDataDictionary['Total_T']=total_t_nuc
    myDataDictionary['Translation']=translation
    dfObj = pd.DataFrame(myDataDictionary)
    dfObj.to_csv("Ncbi_query_1.csv") #Esta función permite guardar en un diccionario todos los datos de los ID guardados previamente y almacenarlos en un DataFrame, para finalmente obtener el archivo .CSV
#Cada que se corra la función y se desee obtener un archivo CSV nuevo, el usuario deberá cambiar el nombre entre comillas, para obtener un nuevo archivo y no sobreescribir el anterior.

def main():
    dic_comandos = diccionario_argumentos() 
    query = dic_comandos['query']
    mail = dic_comandos['mail']
    rec =query_organism(mail, query)
    idlist = rec["IdList"]
    moltype, topology, division, source, organism, taxonomy, sequence, total_a_nuc, total_c_nuc, total_g_nuc, total_t_nuc, locus, strand, id_record, translation = fetch_organism(idlist)
    pandas_cvs(id_record, moltype, locus, strand, topology, division, source, organism, taxonomy, sequence, total_a_nuc, total_g_nuc, total_c_nuc, total_t_nuc, translation)

main()