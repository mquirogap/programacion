import sys
import os
import os.path

#Functions to recover the proteins of each sequence available in file, with the position, translation table, product, protein id, translation sequence and accession number
#according to the sequece each data belongs to.

def getprot(file):
    def get_empty_protein(pos): return {"curr_pos":pos, "transl_table":None, "product":None,"protein_id":None, "translation":None}
    proteinlist=[]
    with open(file) as hdlr:
        previa="gene"
        for line in hdlr:
            if line.startswith("     gene") and previa == "gene":
                previa="gene"
            elif line.startswith("     CDS") and previa == "CDS":
                proteinlist.append(fields)
                fields= get_empty_protein(pos=line[:-1].split()[1])
                previa="CDS"
            elif line.startswith("     gene") and previa == "CDS":
                proteinlist.append(fields)
                fields= get_empty_protein(pos=line[:-1].split()[1])
                previa="gene"
            elif line.startswith("     CDS") and previa == "gene":
                fields= get_empty_protein(pos=line[:-1].split()[1])
                previa="CDS"
            elif line.startswith("ORIGIN"): break
            else:
                if previa == "CDS":
                    values = line[:-1].split()[0].strip()[1:].split('=')
                    if values[0] in fields:
                        if values[0]!= 'translation':
                            fields[values[0]] = values[1]
                        else:
                            translation = values[1][1:]
                            for line in hdlr:
                                line = line.strip()
                                translation +=line
                                if line [-1] == "\"":
                                    break
                            translation = translation[:-1]
                            fields["translation"] = translation
    return proteinlist

def getprot_accession(file):
    accession=[]
    with open(file) as hdlr:
        previa="gene"
        for line in hdlr:
            if line.startswith("ACCESSION"):
                accession_=line.split()[1]
            if line.startswith("     gene") and previa == "gene":
                previa="gene"
            elif line.startswith("     CDS") and previa == "CDS":
                accession.append(accession_)
                previa="CDS"
            elif line.startswith("     gene") and previa == "CDS":
                accession.append(accession_)
                previa="gene"
            elif line.startswith("     CDS") and previa == "gene":
                previa="CDS"
            elif line.startswith("ORIGIN"): 
                previa="CDS"
                break
    return accession