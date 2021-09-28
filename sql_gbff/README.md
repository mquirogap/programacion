# GBFF SQL IMPORT

The following tool contans all the functions needed so that the user can upload important information from a gbff file (.gbff) into a SQL database. The user must provide a gbff file (one at a time), and recover information from the organims, proteins and extended comments that are in the given file. Here you can find the main python file (sql_gbff.py), the source scripts required for the tool to function correctly (organism_functions.py, extended_comments.py and protein_functions.py) and the database file (sql_gbff_databse.db). This program supports both gbff files with a unique accession number or gbff files with multiple accession numbers inside. 

## Description of the SQLite database

The SQLite database contains 3 tables: Organism, Extendedcomments, Protein. 

### Organism table

It's the information that the user can find at the header of each gbff file: accession, base pairs, type of nucleic acid, structure of the sequence, date, definition, completeness of the sequence, source, name and taxonomy.

### Extendedcomments table

It's information that can be foud in the section Genome-Annotation-Data of each gbff file. Each description or item found there has a corresponding value, linked to an accession number.

### Protein table

It's the information of each protein found under the CDS section of each accession available in file: protein_id, position of the gene, translation table, translation sequence, product and the accession number which they are linked to.

## Command line

Below you can find an example of command line for the console so you can run the program with the desired gbff file. 
```python

python3 sql_gbff.py Database='path/sql_gbff_databse.db' Gbff=./data/GCF_000025685.1_ASM2568v1_genomic.gbff #The user must give the path to the database and the path to the gbff file

```

