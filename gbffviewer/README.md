# GBFF VIEWER

La herramienta a continuación contiene todas las funciones necesarias para que el usuario haga búsquedas sobre una carpeta que contenga archivos de interés en formato GBFF (.gbff). A partir de una ruta especificada por el usuario, donde se encuentran todos los archivos .gbff a evaluar, el usuario podrá buscar cuáles archivos contienen un ID específico, ya sea que correspondan a un organismo con un nombre dado, cumplan con un número de accessión o contengan una proteína de interés según el ID de la proteína. Adicionalmente, el usuario puede escoger qué tipo de información quiere recuperar de los archivos que cumplan las características dadas: los nombres de los archivos, el Genome Assembly Data, el header, la secuencia de ADN, la lista de proteínas que contiene o la secuencia de una proteína en particular cuyo ID sea conocido. 

## Descripción

Esta es la lista de comandos necesarios para poder correr el programa

### data

data=./ruta indica la ruta/carpeta donde se encuentran los archivos .gbff que el usuario desea evaluar con la herramienta. 

### ID

La función ID tiene 3 posibles usos:

1. Búsqueda por nombre: id=name:nombre_a_buscar donde se escpecifica el nombre del organismo que se desea encontrar en los archivos. 
2. Búsqueda por accession: id=acc:accession_a_buscar donde se especifica el código de accession con el que fue registrado el archivo. 
3. Búsqueda pro proteína: id=prot:codigo_de_la_proteina_a_buscar donde se especifica el código de la proteína que se desea buscar en los archivo.

### Query

La función query tiene 6 posibles usos:

1. Consultar archivos: query=file permite recuperar el nombre de los archivos que cumplen el ID dado.  
2. Consultar Genome Assembly Data: query=totals permite recuperar los datos de ensamblamiento del genoma de los archivos que cumplen con el ID dado.
3. Consultar encabezado: query=header permite recuperar la información que corresponde a LOCUS, DEFINITION, ACCESSION, VERSION, DBLINK, KEYWORDS, SOURCE, y ORGANISM de los archivos que cumplen con el ID dado.
4. Consultar secuencia de ADN: query=dnaseq permite recuperar la secuencia de ADN de los archivos que cumplen con el ID dado.
5. Consultar lista de proteínas: query=proteinlist permite recuperar la lista de todas las proteínas presentes en los archivos que cumplan con el ID dado.
6. Consultar secuencia de una proteína: para realizar esta consulta es necesario añadir una opción extra en la línea de comandos. Se debe ingresar query=proteinseq protein_seq=codigo_de_la_proteina_a_buscar lo cual permite recuperar la secuencia de la proteína que cumple con el código entregado en protein_seq, dentro de los archivos que cumplen con el ID dado.

## Uso

A continuación se da un ejemplo de como llamar el programa desde la terminal según lo que el usuario desee hacer.
```python


python3 practica_1.py data=./gbff id=acc:JADNRW010000001 query=dnaseq #Obtener secuencia ADN de un accession 
python3 practica_1.py data=./gbff id=acc:JADNRW010000001 query=files #Obtener archivosque tienen un accession 
python3 practica_1.py data=./gbff id=acc:JADNRW010000001 query=totals #Obtener Genome Assembly Data de un accession
python3 practica_1.py data=./gbff id=acc:JADNRW010000001 query=header #Obtener header de un accession
python3 practica_1.py data=./gbff id=acc:JADNRW010000001 query=proteinlist #Obtener lista de proteínas de un accession 
python3 practica_1.py data=./gbff id=acc:JADNRW010000001 query=proteinseq protein_seq=KAF90148 #Obtener secuencia de una proteína en un accession 
#NOTA: para las opciones de query: dnaseq y proteinlist es recomendable adicionar un archivo de salida para poder ver mejor los resultados ( >output.txt)
python3 practica_1.py data=./gbff id=acc:JADNRW010000001 query=proteinlist >output.txt
```
