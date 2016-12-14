import sys 
myfile = open(sys.argv[1], "r")	#open the file with your list of samples to use in cstacks
newfile = open("new_cstacks_code", "w")	#create a new file where the ustacks code will go
newfile.write("#!/bin/bash\n")
filestring = "cstacks -b 123 "
for line in myfile: 			#for each line in the barcode file
	sampID = line.strip()	
	if sampID.startswith("#"): 
		newstring = ""
	else: 	
		linelist = line.strip().split(".")		
		newSampID = ".".join(linelist[0:2])
		newstring = "-s ./" + newSampID + " "
	filestring += newstring
filestring += "-o stacks -n 3 -p 6"
newfile.write(filestring)
myfile.close()
newfile.close()
