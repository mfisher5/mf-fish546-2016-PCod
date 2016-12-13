#### To find the SNPs in multiple sequences ####
## input file: locus <tab> SNP_location <tab> sequence


import sys
seqfile = open(sys.argv[1], "r")
for line in seqfile:
	linelist = line.strip().split()
	seq = list(linelist[2])
	i = int(linelist[1]) - 1
	print "Locus: ", linelist[0], "SNP location: ", linelist[1], "SNP: ", seq[i]
