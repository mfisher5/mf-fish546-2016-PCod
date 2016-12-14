import sys
batchFile = open(sys.argv[1], "r")
Filestring = batchFile.readline()
numLoci = Filestring.count(",")
print "The number of loci in ", sys.argv[1], "is: ", numLoci
