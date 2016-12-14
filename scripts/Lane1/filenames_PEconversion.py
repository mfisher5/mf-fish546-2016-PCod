import sys
myfile = open(sys.argv[1], "r")
new_file1 = open("new_filenames1.txt", "w")
new_file2 = open("new_filenames2.txt", "w")
for line in myfile: 
	linelist=line.strip().split()
	barcodefile = "sample_" + linelist[1] + ".1.fa.gz"
	samplefile = linelist[2] + ".1.fa.gz"
	newstring1 = linelist[0] + "\t" + barcodefile + "\t" + samplefile + "\n"
	new_file1.write(newstring1)
	barcodefile = "sample_" + linelist[1] + ".2.fa.gz"
	samplefile = linelist[2] + ".2.fa.gz"
	newstring2 = linelist[0] + "\t" + barcodefile + "\t" + samplefile + "\n"
	new_file2.write(newstring2)
new_file2.close()
myfile.close()
new_file1.close()
