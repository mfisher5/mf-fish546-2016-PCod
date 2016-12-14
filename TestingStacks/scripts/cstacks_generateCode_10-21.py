import sys 
myfile = open(sys.argv[1], "r")	#open the file with your list of samples to use in cstacks
newfile = open("new_cstacks_code", "w")	#create a new file where the ustacks code will go
newfile.write("#!/bin/bash\n")
filestring = "cstacks -b 303 "
for line in myfile: 			#for each line in the barcode file
	sampID = line.strip()	
	if sampID.startswith("#"): 
		newstring = ""
	else: 	
		linelist = line.strip().split(".")		
		newSampID = ".".join(linelist[0:2])
		newstring = "-s stacks_base/" + newSampID + " "
	filestring += newstring
myfile.close()
filestring += "-o stacks_base -n 3 -p 6"
newfile.write(filestring)
newfile.write("\n\n")



myfile = open(sys.argv[1], "r")
filestring = "cstacks -b 300 "
for line in myfile: 			#for each line in the barcode file
	sampID = line.strip()	
	if sampID.startswith("#"): 
		newstring = ""
	else: 	
		linelist = line.strip().split(".")		
		newSampID = ".".join(linelist[0:2])
		newstring = "-s stacks_base/" + newSampID + " "
	filestring += newstring
myfile.close()
filestring += "-o stacks_base -n 0 -p 6"
newfile.write(filestring)
newfile.write("\n\n")




myfile = open(sys.argv[1], "r")
filestring = "cstacks -b 230 "
for line in myfile: 			#for each line in the barcode file
	sampID = line.strip()	
	if sampID.startswith("#"): 
		newstring = ""
	else: 	
		linelist = line.strip().split(".")		
		newSampID = ".".join(linelist[0:2])
		newstring = "-s stacks_M2/" + newSampID + " "
	filestring += newstring
myfile.close()
filestring += "-o stacks_M2 -n 3 -p 6"
newfile.write(filestring)
newfile.write("\n\n")




myfile = open(sys.argv[1], "r")
filestring = "cstacks -b 330 "
for line in myfile: 			#for each line in the barcode file
	sampID = line.strip()	
	if sampID.startswith("#"): 
		newstring = ""
	else: 	
		linelist = line.strip().split(".")		
		newSampID = ".".join(linelist[0:2])
		newstring = "-s stacks_m3/" + newSampID + " "
	filestring += newstring
myfile.close()
filestring += "-o stacks_m3 -n 3 -p 6"
newfile.write(filestring)
newfile.write("\n\n")




myfile = open(sys.argv[1], "r")
filestring = "cstacks -b 1030 "
for line in myfile: 			#for each line in the barcode file
	sampID = line.strip()	
	if sampID.startswith("#"): 
		newstring = ""
	else: 	
		linelist = line.strip().split(".")		
		newSampID = ".".join(linelist[0:2])
		newstring = "-s stacks_m10/" + newSampID + " "
	filestring += newstring
myfile.close()
filestring += "-o stacks_m10 -n 3 -p 6"
newfile.write(filestring)
newfile.write("\n\n")


