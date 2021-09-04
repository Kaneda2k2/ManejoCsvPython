




###################################  LEEEEEEER CSV


##import csv
##
##exampleFile = open('example.csv')
##exampleRead=csv.reader(exampleFile)
##exampledata=list(exampleRead)
##
##
##
##print(exampledata[1][2])
##print(exampledata)

##print(exampledata)
##print(exampledata)
##print(exampledata)

####################################################

###########################READING DATA FROM READER OBJECT IN A FOR LOOP
##
##import csv
##exampleFile=open("example.csv")
##exampleReader=csv.reader(exampleFile)
##for row in exampleReader:
##    print("Row#"+str(exampleReader.line_num)+""+str(row))

#######################################################################

#################           Writer objects

##import csv
##outputFile=open("output1.csv","w",newline="")
##outputWriter=csv.writer(outputFile)
##outputWriter.writerow(["spam","eggs","bacon","ham"])
##outputWriter.writerow(["Hello world","eggs","bacon","ham"])
##outputWriter.writerow(["1","2","3.142312","4"])
##outputFile.close()

##################################################


##import csv
##csvFile=open("example.csv","w",newline="")
##csvWriter=csv.writer(csvFile,delimiter="\t",lineterminator="\n\n")
##csvWriter.writerow(['apples', 'oranges', 'grapes'])
##csvWriter.writerow(['eggs', 'bacon', 'ham'])
##
##csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
##
##csvFile.close()
##


#########################################################
################################ CSV CON CABEZERA
##Si tiene cabecera es mas conveniente trabajar con dictreader and dictwriter objects

##import csv
##
##exampleFile=open("exampleWithHeader.csv")
##exampleDictReader=csv.DictReader(exampleFile)
##for row in exampleDictReader:
##    print(row["Timestamp"],row["Fruit"],row["Quantity"])
##

#########################CSV SIN CABEZERA PERO PONIENDO CABEZERA PROVICIONAL
##import csv
##exampleFile=open("example.csv")
##exampleDictReader=csv.DictReader(exampleFile,["time","name","amount"])
##
##for row in exampleDictReader:
##    print(row["time"],row["name"],row["amount"]

##############################################################
#####################CREAR CABEZERA Y AÑADIR DATOS EN FORMATO DICCIONARIO PARA QUE LO COJA LA CABEZERA

##import csv
##outputFile=open("output.csv","w",newline="")
##outputDictWriter=csv.DictWriter(outputFile,["Name","Pet","Phone"])   #Creanos cabezera
##outputDictWriter.writeheader()
##outputDictWriter.writerow({"Name":"Alice","Pet":"cat","Phone":"555-1234"})
##
##outputDictWriter.writerow({"Name":"Bob","Phone":"555-9999"})
##
##outputDictWriter.writerow({"Phone":"555-5555","Name":"Carlos","Pet":"dog"})
##outputFile.close()


########################################################

                ###PROJECT : REMOVING THE HEADER FROM CSV FILES


#programa tendria que abrir todas las filas  con csv extension in the current working directory
#read the contents csv and rewrite the contect wigotut rhw first row to a file of the same name
#this will replace the old co

#siempre que haces un programa que modifica filas estate seguro de hacer un backip a los documentos primero

#1 encontrar todos los csv
#2Read in the full contect of each file
#3 Write out the contents ,skipping the first line , to a new CSV file

#----------------------------------------------------
#loop over a list of files from os.listdir(),skipping the non-csv files.
#Create a csv reader object and read in the contects of the file,
#using line_num attribute to figure out which line to skip
#Create CSV writes object and write out the read in data to the new file

#for this project open a new file editor windows and save it as removeCsvHeader










