#!python3
#removerCSVHeader - Removes the header from all csv files in the current working directory

import csv,os

os.makedirs("headerRemover",exist_ok=True)  #Crea carpeta y si esta creada no hace nada

#Loop throug every file in the current working directory.
for csvFilename in os.listdir("."):       #
    if not csvFilename.endswith(".csv"):
        continue  # skip non-csv files

    print("Removing header from" + csvFilename + " ")

    #TODO: Read the CSV file in (skipping first row).
    csvRows=[]                 #va a contener todos los rows
    csvFileObj=open(csvFilename)      #se abre el documento
    readerObj=csv.reader(csvFileObj)    ### se lee el objeto
    for row in readerObj:              #por cada  fila en el objeto
        if readerObj.line_num==1:     # se lee la linea numero 1
            continue #skip first row
        csvRows.append(row)           #
    csvFileObj.close()


    #TODO: Write out the CSV file

    csvFileObj=open(os.path.join("headerRemover",csvFilename),"w",newline="")

    csvWriter=csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()