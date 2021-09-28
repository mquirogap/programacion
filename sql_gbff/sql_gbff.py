from organism_functions import *
from extended_comments_functions import *
from protein_functions import *
import sys
import os
import os.path
import sqlite3 as sql

#Dictionary function, allows the user to save query options, to know where the databse and the filepath are

def import_files():
    arguments={}
    if len(sys.argv) < 3:
        print(" Not enough arguments are given. The sintaxis is <Database=path> <Gbff=filepath>, in that order")
        return {}
    else:
        for p in sys.argv[1:]:
            option = p.split("=")[0] 
            value_option = p.split("=")[1] 
            arguments[option] = value_option
        return arguments

#Get the database and the gbff file from the options the user gave

files=import_files()
database=files["Database"]
gbff=files['Gbff']

#Variables for Organism functions so they can be inserted into the database

accession= accession_in_file(gbff)
base_pairs= base_pairs_in_file(gbff)
tipo=tipo_in_file(gbff)
structure=structure_in_file(gbff)
date=date_in_file(gbff)
definitions=definition(gbff)
completeness_= completeness(gbff)
source_= source(gbff)
name= name_in_file(gbff)
taxonomy_= taxonomy(gbff)

#Variables for Protein functions so they can be inserted into the database

proteins =getprot(gbff)
prot_accession=getprot_accession(gbff)
protein_id=[]
curr_pos=[]
transl_table=[]
translation_=[]
product=[]
for protein in proteins:
    protein_id.append(protein["protein_id"])
    curr_pos.append(protein["curr_pos"])
    transl_table.append(protein["transl_table"])
    translation_.append(protein["translation"])
    product.append(protein["product"])

#Variables for Extended comments so they can be inserted into the database

accession_comments=comments(gbff)[2]
description_comments=comments(gbff)[0]
value_comments=comments(gbff)[1]

#SQLITE

conn=sql.connect(database)

#Protein table
for i in range(0,len(prot_accession)):
    insertions = [(protein_id[i], prot_accession[i], curr_pos[i], transl_table[i], translation_[i], product[i])]
    conn.executemany('INSERT INTO Protein VALUES (?,?,?,?,?,?)', insertions)

#Organism table

for i in range (0, len(accession)):
    o = [(accession[i], base_pairs[i], tipo[i], structure[i], date[i], definitions[i], completeness_[i], source_[i], name[i], taxonomy_[i])]
    conn.executemany('INSERT INTO Organism VALUES (?,?,?,?,?,?,?,?,?,?)', o)

#Extendedcomments table

for i in range (0,len(accession_comments)):
    insertions_c = [(accession_comments[i], description_comments[i], value_comments[i])]
    conn.executemany('INSERT INTO Extendedcomments VALUES (?,?,?)', insertions_c)

#Register the data and close the conection with the database when all changes are ready
conn.commit()
conn.close()

