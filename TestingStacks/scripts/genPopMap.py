
#command line: 
#python <filename_samples> <pop1 name> <pop2 name> etc. 

import sys

npops = len(sys.argv) - 2
poplist = []
i = 1
while i <= npops: 
	poplist.append(sys.argv[i+1])
	i += 1
print "Populations: ", poplist

## create a new file for the population map
popmap = open("PopulationMap.txt", "w")

## add to the population map file: sampleID <tab> population
namefile = open(sys.argv[1], "r")
for line in namefile:
	linelist = line.strip().split()
	count = 0
	while count <= (npops-1):
		if linelist[2].startswith(poplist[count][0:1]):
			popmap.write(linelist[2] +".1" "\t" + str(poplist[count]) + "\n")
		else:	
			popmap.write("")
		count += 1
namefile.close()
popmap.close()
num_lines = sum(1 for line in open('PopulationMap.txt'))
print "Population Map generated with ", num_lines, "samples"

	
	

