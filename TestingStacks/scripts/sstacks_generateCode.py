import sys 
myfile = open(sys.argv[1], "r")	#open the file with your list of samples to use in cstacks
newfile = open("sstacks_batch300_shell", "w")	#create a new file where the ustacks code will go
newfile.write("#/bin/bash" + "\n")
filestring = "sstacks -b 300 -c stacks_base/batch_300 " #choose batch ID and catalog files
for line in myfile: 			#for each line in the barcode file
	linelist=line.strip().split()	
	samplefile = linelist[2] + ".1"		#creates name of sample input file based on sample list in myfile
	newstring = "-s stacks_base/" + samplefile + " "	#creates a new -s entry for that sample input file
	filestring += newstring			# appends new -s string to "filestring"
filestring += "-o sstacks_batch300 -p 6 2>> sstacks_out_b300"   #choose output folder and processor # and std.err out file
newfile.write(filestring)		#write entire string to the new file
myfile.close()
newfile.close()

