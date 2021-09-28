import sys
import os
import os.path

#Function to recover the Genome-Annotation-Data from the sequences in the gbff file

def comments(file):
    field=[]
    annotation=[]
    accession=[]
    with open(file) as hdlr:
        key=False
        for line in hdlr:
            if line.startswith("ACCESSION"):
                accession_=line.split()[1]
            if "Data-START##" in line:
                key=True
                continue
            elif "Data-END##" in line:
                key=False
                continue
            elif key :
                if "::" in line:
                    field.append(line.split(" :: ")[0])
                    field=[x.strip("            ") for x in field]
                    annotation.append(line.split(":: ")[1])
                    annotation=[x.strip("\n") for x in annotation]
                    accession.append(accession_ )
    return field, annotation, accession