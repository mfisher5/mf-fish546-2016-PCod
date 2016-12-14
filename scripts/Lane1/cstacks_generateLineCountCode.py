import sys 
myfile = open(sys.argv[1], "r")	#open the file with your list of barcodes and sample IDs
newfile = open("new_cstacks_linecount", "w")	#create a new file where the ustacks code will go
newfile2 = open("new_cstacks_linecountSamples","w")
filestring = ""
for line in myfile: 			#for each line in the barcode file
	linelist = line.strip().split()	
	sampID = linelist[2]
	newfile2.write(sampID + ".1.fa.gz\n")
	newstring = "zcat " + sampID + ".1.fa.gz | wc -l >> ../new_LineCounts.txt\n"
	filestring += newstring
myfile.close()
newfile2.close()
newfile.write(filestring)
newfile.close()


