#### Counts the number of unique loci in a text file containing the header of a .genepop file (Locus_SNP). To be used after running populations, to determine how many loci were retained ####

## MF 12/12/2016




import sys
batchFile = open(sys.argv[1], "r")

#read row of loci names into a string
Filestring = batchFile.read()

lociList = Filestring.split(",")
UniqueLoci = []
for locus in lociList:
	templocus = locus.split("_")
	if templocus[0] not in UniqueLoci:
		UniqueLoci.append(templocus[0])

#count the number of loci in the UniqueLoci list
print "The number of unique loci in ", sys.argv[1], "is: ", len(UniqueLoci)
