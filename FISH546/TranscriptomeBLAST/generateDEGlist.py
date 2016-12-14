import sys 
DEGfile = open(sys.argv[1], "r")
newfile = open("Phel_DEGnames.txt", "w")
for line in DEGfile: 
	linelist = line.strip().split(" ")
	newfile.write(linelist[0] + "\n")
DEGfile.close()
newfile.close()
