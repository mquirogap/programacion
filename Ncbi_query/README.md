# NCBI query tool

The following tool allows the user to enter a specific NCBI query and get back s .CSV file with the main information contained there: id record, molecule type, locus, length, strandedness, topology, division, source, organism, taxonomy and sequence. The user must provide an e-mail and the NCBI query as it is written in the "Search details" box at the NCBI page. Here you can find the main python file Ncbi_query.py. 

## Query options

For the user to enter the query it is necessary that the statement is between quotation marks and each time there is a quotation mark inside the query a backslash is required, so the command can be correctly received, as seen below: 
### Query in the search details box

"Moniliophthora perniciosa"[Organism] OR Moniliophthora perniciosa[All Fields]

### Query in the command line

" \ "Moniliophthora perniciosa \ "[Organism] OR moniliophthora perniciosa[All Fields]"

## Command line

Below you can find an example of command line for the console so you can run the program with the desired gbff file. 
```python

python3 ncbi_query.py mail=mail@gmail.com query="\"Moniliophthora perniciosa\"[Organism] OR moniliophthora perniciosa[All Fields]" #The user must give an specific query and an e-mail

```


