import sys
import os
import os.path

#Function to recover all accessions available in the gbff file

def accession_in_file(file):
    accession=[]
    with open(file) as hdlr:
        for line in hdlr:
            if line.startswith("ACCESSION"):
                accession.append(line.split()[1])
    return accession

#Function to recover all the base_pairs from all sequences in the gbff file

def base_pairs_in_file(file):
    base_pairs=[]
    with open(file) as hdlr:
        for line in hdlr:
            if line.startswith("LOCUS"):
                base_pairs.append(line.split()[2])
    return base_pairs

#Function to recover the type of nucleic acid of all the sequences in the gbff file

def tipo_in_file(file):
    tipo=[]
    with open(file) as hdlr:
        for line in hdlr:
            if line.startswith("LOCUS"):
                tipo.append(line.split()[4])
    return tipo

#Function to recover the type of structure (linear or circular) of the sequences in the gbff file

def structure_in_file(file):
    structure=[]
    with open(file) as hdlr:
        for line in hdlr:
            if line.startswith("LOCUS"):
                structure.append(line.split()[5])
    return structure

#Function to recover the date of the sequences in file

def date_in_file(file):
    date=[]
    with open(file) as hdlr:
        for line in hdlr:
            if line.startswith("LOCUS"):
                date.append(line.split()[7])
    return date

#Function to recover all the definitions of the sequences in the gbff file

def definition(file):
    definition=[]
    with open(file) as hdlr:
        key=False
        for line in hdlr:
            if "DEFINITION" in line:
                key=True
                definition.append((line.lstrip('DEFINITION  ')[:-1]))
                continue
            elif "ACCESSION" in line:
                key=False
                continue
            elif key==True:
                definition.append(" " + line.lstrip()[:-1])
    definition_list=''.join(map(str,definition))
    definition_list_complete=definition_list.split(".")[:-1]
    return definition_list_complete

#Functions to recover weather or not the completeness of the sequence is specified in file and if it is a complete sequence or not. 

def completeness_in_file(file):
    with open(file) as hdlr:
        for line in hdlr:
            if "COMPLETENESS" in line:
                return True


def completeness(file):
    completeness=[]
    with open(file) as hdlr:
        if completeness_in_file(file):
            for line in hdlr:
                if "COMPLETENESS" in line:
                    completeness.append(line.split(": ")[1][:-2]) 
                    continue
        else:
            for line in hdlr:
                if "COMMENT" in line:
                    completeness.append(" ")
                    continue
    return completeness

#Function to recover the source of the sequences in file

def source(file):
    source=[]
    with open(file) as hdlr:
        for line in hdlr:
            if line.startswith("SOURCE"):
                source.append(line.lstrip('SOURCE')[:-1])
                source = [x.strip(' ') for x in source]
    return source

#Function to recover the name of the organisms of the sequences in file

def name_in_file(file):
    name=[]
    with open(file) as hdlr:
        for line in hdlr:
            if "ORGANISM" in line:
                name.append(line)
                name = [x.strip(' ') for x in name]
                names = [s.replace("ORGANISM", "") for s in name]
                names = [x.strip(' ')[:-1] for x in names]
    return names

#Function to recover the taxonomy of the sequecenes in the gbff file

def taxonomy(file):
    taxonomy=[]
    with open(file) as hdlr:
        copy=False
        for line in hdlr:
            if "ORGANISM" in line:
                copy=True
                continue
            elif "REFERENCE" in line:
                copy=False
            elif copy:
                taxonomy.append(line[:-1])
                taxonomy=[x.strip("            ") for x in taxonomy]
    taxonomy_list=''.join(map(str,taxonomy))
    taxonomy_list_complete=taxonomy_list.split(".")[:-1]
    return taxonomy_list_complete
